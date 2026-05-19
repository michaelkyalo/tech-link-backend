from flask_restful import Resource
from flask import request
from app.services.payment_service import PaymentService
from app.models.payment_model import Payment


class PaymentListResource(Resource):

    def post(self):
        data = request.get_json()

        payment, error = PaymentService.create_payment(data)

        if error:
            return {"message": error}, 400

        return {
            "message": "Payment successful",
            "payment": {
                "id": payment.id,
                "order_id": payment.order_id,
                "amount": payment.amount,
                "payment_method": payment.payment_method,
                "payment_status": payment.payment_status,
                "transaction_id": payment.transaction_id
            }
        }, 201


class PaymentResource(Resource):

    def get(self, payment_id):

        payment = Payment.query.get(payment_id)

        if not payment:
            return {"message": "Payment not found"}, 404

        return {
            "id": payment.id,
            "order_id": payment.order_id,
            "amount": payment.amount,
            "payment_method": payment.payment_method,
            "payment_status": payment.payment_status,
            "transaction_id": payment.transaction_id
        }, 200