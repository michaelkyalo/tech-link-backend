from app.config.database import db
from app.models.payment_model import Payment
from app.models.order_model import Order

class PaymentService:
    @staticmethod
    def create_payment(data):
        order = Order.query.get(data["order_id"])
        if not order:
            return None, "Order not found"

        payment = Payment(
            order_id=data["order_id"],
            amount=data["amount"],
            payment_method=data["payment_method"],
            payment_status=data.get("payment_status", "pending"),
            transaction_code=data.get("transaction_code")  # ← was transaction_id
        )

        db.session.add(payment)
        db.session.commit()
        return payment, "Payment created successfully"