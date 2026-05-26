from datetime import datetime
from app.config.database import db


class Order(db.Model):

    __tablename__ = "orders"

    order_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    buyer_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    total_amount = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    payment_method = db.Column(
        db.String(50),
        nullable=True
    )

    delivery_address = db.Column(
        db.String(255),
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Order {self.order_id}>"