from datetime import datetime

from app.config.database import db


class Payment(db.Model):

    __tablename__ = "payments"

    payment_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    order_id = db.Column(
        db.BigInteger,
        db.ForeignKey("orders.order_id"),
        nullable=False
    )

    amount = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    payment_method = db.Column(
        db.String(50),
        nullable=False
    )

    transaction_code = db.Column(
        db.String(255)
    )

    payment_status = db.Column(
        db.String(30),
        default="pending"
    )

    paid_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Payment {self.payment_id}>"