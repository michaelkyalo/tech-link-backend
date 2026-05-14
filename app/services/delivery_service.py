from app.models.delivery_model import Delivery
from app.config.database import db


def create_delivery(data):
    required_fields = ["order_id", "address"]

    for field in required_fields:
        if field not in data:
            return None, f"{field} is required"

    delivery = Delivery(
        order_id=data["order_id"],
        address=data["address"],
        status="pending"
    )

    db.session.add(delivery)
    db.session.commit()

    return delivery.to_dict(), None


def get_delivery_by_order(order_id):
    delivery = Delivery.query.filter_by(order_id=order_id).first()

    if not delivery:
        return None

    return delivery.to_dict()


def update_delivery_status(delivery_id, data):
    delivery = Delivery.query.get(delivery_id)

    if not delivery:
        return None, "Delivery not found"

    if "status" in data:
        delivery.status = data["status"]

    db.session.commit()

    return delivery.to_dict(), None