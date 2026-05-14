from flask import Blueprint, request, jsonify
from app.services.order_item_service import (
    add_item_to_order,
    remove_item_from_order
)

order_item_bp = Blueprint("order_item_bp", __name__)


@order_item_bp.route("/order-items", methods=["POST"])
def add_item():
    data = request.get_json()
    item, error = add_item_to_order(data)

    if error:
        return jsonify({"message": error}), 400

    return jsonify({"message": "Item added", "item": item}), 201


@order_item_bp.route("/order-items/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):
    success, error = remove_item_from_order(item_id)

    if error:
        return jsonify({"message": error}),

    return jsonify({"message": "Item removed"}),