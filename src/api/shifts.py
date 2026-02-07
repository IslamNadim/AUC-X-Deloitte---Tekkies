from flask import Blueprint, request, jsonify
from db import get_connection
from auth import require_api_key

shifts_bp = Blueprint("shifts", __name__)

@shifts_bp.route("/optimize", methods=["POST"])
@require_api_key
def optimize_shifts():
    data = request.get_json()
    place_id = data.get("place_id")

    if not place_id:
        return jsonify({"error": "place_id required"}), 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*) FROM orders WHERE place_id = %s
    """, (place_id,))
    orders_count = cur.fetchone()[0]

    cur.close()
    conn.close()

    staff_needed = max(1, orders_count // 20)

    return jsonify({
        "place_id": place_id,
        "recommended_staff": staff_needed,
        "estimated_coverage": 0.9
    })
