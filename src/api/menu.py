from flask import Blueprint, request, jsonify
from db import get_connection
from auth import require_api_key

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/analyze", methods=["POST"])
@require_api_key
def analyze_menu():
    data = request.get_json()
    place_id = data.get("place_id")

    if not place_id:
        return jsonify({"error": "place_id required"}), 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT mi.title,
               SUM(oi.quantity) AS popularity,
               AVG(oi.price - oi.cost) AS profit
        FROM order_items oi
        JOIN menu_items mi ON mi.item_id = oi.item_id
        JOIN orders o ON o.order_id = oi.order_id
        WHERE o.place_id = %s
        GROUP BY mi.title
    """, (place_id,))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    stars, plowhorses, puzzles, dogs = [], [], [], []

    for title, popularity, profit in rows:
        item = {"title": title, "popularity": popularity, "profit": float(profit)}

        if popularity > 50 and profit > 5:
            stars.append(item)
        elif popularity > 50:
            plowhorses.append(item)
        elif profit > 5:
            puzzles.append(item)
        else:
            dogs.append(item)

    return jsonify({
        "stars": stars,
        "plowhorses": plowhorses,
        "puzzles": puzzles,
        "dogs": dogs
    })


from flask import Blueprint, request, jsonify
from db import get_connection
from auth import require_api_key
import pandas as pd

# import ML function
from ml.clustering import menu_engineering_clusters
from ai.assistant import generate_menu_insights

menu_bp = Blueprint("menu", __name__)


@menu_bp.route("/cluster", methods=["POST"])
@require_api_key
def cluster_menu():
    """
    Runs menu engineering clustering (Star, Plowhorse, Puzzle, Dog)
    based on real sales and profit data.
    """

    try:
        data = request.get_json()
        place_id = data.get("place_id")

        if not place_id:
            return jsonify({"error": "place_id required"}), 400

        # ---- Load menu performance from DB ----
        conn = get_connection()
        query = """
            SELECT
                mi.title,
                COALESCE(SUM(oi.quantity), 0) AS Sales_Volume,
                COALESCE(SUM((oi.price - oi.cost) * oi.quantity), 0) AS Profit
            FROM menu_items mi
            LEFT JOIN order_items oi ON mi.item_id = oi.item_id
            LEFT JOIN orders o ON oi.order_id = o.order_id
            WHERE o.place_id = %s OR o.place_id IS NULL
            GROUP BY mi.title
        """

        df = pd.read_sql(query, conn, params=(place_id,))

        # Normalize column names for ML
        df = df.rename(columns={
            "sales_volume": "Sales_Volume",
            "profit": "Profit"
        })

        conn.close()

        if df.empty:
            return jsonify({"error": "No menu data found"}), 404

        # ---- Run ML clustering ----
        df = menu_engineering_clusters(df)

        # ---- Return JSON ----
        return jsonify(df.to_dict(orient="records"))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@menu_bp.route("/cluster/insights", methods=["POST"])
@require_api_key
def cluster_insights():
    try:
        data = request.get_json()
        place_id = data.get("place_id")

        if not place_id:
            return jsonify({"error": "place_id required"}), 400

        # ---- Load clustered menu ----
        conn = get_connection()

        query = """
        SELECT title, Sales_Volume, Profit, menu_category
        FROM menu_engineering_view
        WHERE place_id = %s
        """

        df = pd.read_sql(query, conn, params=(place_id,))
        conn.close()

        if df.empty:
            return jsonify({"error": "No menu data"}), 404

        # ---- Convert to records ----
        records = df.to_dict(orient="records")

        # ---- Generate AI insights ----
        result = generate_menu_insights(records)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500