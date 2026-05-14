from flask import Blueprint, request, jsonify
from app.services.delivery_service import (
    create_delivery,
    get_delivery_by_order,
    update_delivery_status
)

delivery_bp = Blueprint("delivery_bp", __name__)


@delivery_bp.route("/deliveries", methods=["POST"])
def create_new_delivery():
    data = request.get_json()
    delivery, error = create_delivery(data)

    if error:
        return jsonify({"message": error}),

    return jsonify({
        "message": "Delivery created",
        "delivery": delivery
    }), 201


@delivery_bp.route("/deliveries/order/<int:order_id>", methods=["GET"])
def fetch_delivery_by_order(order_id):
    delivery = get_delivery_by_order(order_id)

    if not delivery:
        return jsonify({"message": "Delivery not found"}), 404

    return jsonify(delivery), 


@delivery_bp.route("/deliveries/<int:delivery_id>", methods=["PATCH"])
def update_status(delivery_id):
    data = request.get_json()
    updated, error = update_delivery_status(delivery_id, data)

    if error:
        return jsonify({"message": error}),

    return jsonify({
        "message": "Delivery status updated",
        "delivery": updated
    }), 