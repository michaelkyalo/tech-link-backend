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

    total_price = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    order_status = db.Column(
        db.String(30),
        default="pending"
    )

    payment_status = db.Column(
        db.String(30),
        default="pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    order_items = db.relationship(
        "OrderItem",
        backref="order",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):

        return f"<Order {self.order_id}>"