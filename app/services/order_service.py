from app.config.database import db
from app.models.order_model import Order

class OrderService:

    @staticmethod
    def create_order(data):
        order = Order(
            buyer_id=data["buyer_id"],
            total_amount=data["total_amount"],
            delivery_address=data["delivery_address"]
        )

        db.session.add(order)
        db.session.commit()

        return order

    @staticmethod
    def get_all_orders(page=1, per_page=10):
        return Order.query.paginate(page=page, per_page=per_page)

    @staticmethod
    def get_order_by_id(order_id):
        
        return Order.query.get(order_id)

    @staticmethod
    def update_order(order, data):
        

        order.order_status = data.get("order_status", order.order_status)
        order.delivery_address = data.get("delivery_address", order.delivery_address)

        db.session.commit()
        return order

    @staticmethod
    def delete_order(order):

        db.session.delete(order)
        db.session.commit()