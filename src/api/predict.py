from flask import Blueprint, request, jsonify
from db import get_connection
from auth import require_api_key

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
@require_api_key
def predict_demand():
    data = request.get_json()
    item_id = data.get("item_id")

    if not item_id:
        return jsonify({"error": "item_id required"}), 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COALESCE(SUM(quantity), 0)
        FROM order_items
        WHERE item_id = %s
    """, (item_id,))

    total_sales = cur.fetchone()[0]

    cur.close()
    conn.close()

    prediction = total_sales * 1.1  # simple growth model

    return jsonify({
        "item_id": item_id,
        "predicted_demand": float(prediction),
        "confidence": 0.75
    })
