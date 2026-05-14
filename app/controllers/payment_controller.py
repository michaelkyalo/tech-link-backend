from flask import Blueprint, request, jsonify
from app.services.payment_service import process_payment, get_payment_status

payment_bp = Blueprint("payment_bp", __name__)


@payment_bp.route("/payments", methods=["POST"])
def make_payment():
    data = request.get_json()
    payment, error = process_payment(data)

    if error:
        return jsonify({"message": error}), 

    return jsonify({"message": "Payment successful", "payment": payment}),


@payment_bp.route("/payments/<int:payment_id>", methods=["GET"])
def payment_status(payment_id):
    payment = get_payment_status(payment_id)

    if not payment:
        return jsonify({"message": "Payment not found"}),

    return jsonify(payment),