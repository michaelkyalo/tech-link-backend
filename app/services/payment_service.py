from app.config.database import db
from app.models.payment_model import Payment
from app.models.order_model import Order


class PaymentService:

    @staticmethod
    def create_payment(data):
        """
        Create a payment linked to an order.
        """

        order = Order.query.get(data["order_id"])
        if not order:
            return None, "Order not found"

        payment = Payment(
            order_id=data["order_id"],
            amount=data["amount"],
            payment_method=data["payment_method"],
            payment_status=data.get("payment_status", "pending"),
            transaction_id=data.get("transaction_id")
        )

        db.session.add(payment)
        db.session.commit()

        return payment, "Payment created successfully"

    @staticmethod
    def get_payment_by_id(payment_id):
        return Payment.query.get(payment_id)

    @staticmethod
    def get_all_payments(page=1, per_page=10):
        return Payment.query.paginate(page=page, per_page=per_page)

    @staticmethod
    def update_payment(payment, data):
        """
        Update payment status or details.
        """

        payment.payment_status = data.get(
            "payment_status",
            payment.payment_status
        )

        payment.transaction_id = data.get(
            "transaction_id",
            payment.transaction_id
        )

        db.session.commit()

        return payment, "Payment updated successfully"

    @staticmethod
    def delete_payment(payment):
        db.session.delete(payment)
        db.session.commit()

        return True, "Payment deleted successfully"