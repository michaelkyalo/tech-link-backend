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

    def __repr__(self):

        return f"<Delivery {self.delivery_id}>"