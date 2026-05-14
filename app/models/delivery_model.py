from datetime import datetime
from app.config.database import db


class Delivery(db.Model):

    __tablename__ = "deliveries"

    delivery_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    order_id = db.Column(
        db.BigInteger,
        db.ForeignKey("orders.order_id"),
        nullable=False
    )

    delivery_method = db.Column(
        db.String(50),
        nullable=False
    )

    delivery_status = db.Column(
        db.String(50),
        default="pending"
    )

    pickup_location = db.Column(
        db.String(255)
    )

    destination_location = db.Column(
        db.String(255)
    )

    delivery_date = db.Column(
        db.DateTime
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    order = db.relationship(
        "Order",
        backref="deliveries"
    )

    def __repr__(self):

        return f"<Delivery {self.delivery_id}>"

    def to_dict(self):

        return {
            "delivery_id": self.delivery_id,
            "order_id": self.order_id,
            "delivery_method": self.delivery_method,
            "delivery_status": self.delivery_status,
            "pickup_location": self.pickup_location,
            "destination_location": self.destination_location,
            "delivery_date": self.delivery_date,
            "created_at": self.created_at
        }