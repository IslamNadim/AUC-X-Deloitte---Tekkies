from flask import Blueprint, jsonify
from db import get_connection
from auth import require_api_key

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/items", methods=["GET"])
@require_api_key
def get_items():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT item_id, title, COALESCE(avg_price, 0), COALESCE(avg_cost, 0) FROM menu_items")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    items = [
        {
            "item_id": r[0],
            "title": r[1],
            "avg_price": float(r[2]),
            "avg_cost": float(r[3]),
        }
        for r in rows
    ]

    return jsonify(items)
