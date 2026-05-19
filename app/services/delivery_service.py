from app.config.database import db
from app.models.delivery_model import Delivery

class DeliveryService:

    @staticmethod
    def create_delivery(data):
        
        for field in ["order_id", "address"]:
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

    @staticmethod
    def get_delivery_by_order(order_id):

        delivery = Delivery.query.filter_by(order_id=order_id).first()
        return delivery.to_dict() if delivery else None

    @staticmethod
    def update_delivery_status(delivery_id, data):
      

        delivery = Delivery.query.get(delivery_id)

        if not delivery:
            return None, "Delivery not found"

        if "status" in data:
            delivery.status = data["status"]

        db.session.commit()

        return delivery.to_dict(), None