from app.config.database import db
from app.models.order_item_model import OrderItem
from app.models.order_model import Order
from app.models.product_model import Product
class OrderItemService:

    @staticmethod
    def create_order_item(data):
        
        order = Order.query.get(data["order_id"])
        if not order:
            return None, "Order not found"

        product = Product.query.get(data["product_id"])
        if not product:
            return None, "Product not found"

        if product.stock_quantity < data["quantity"]:
            return None, "Insufficient stock"

        quantity = data["quantity"]
        subtotal = product.price * quantity

        order_item = OrderItem(
            order_id=data["order_id"],
            product_id=data["product_id"],
            quantity=quantity,
            unit_price=product.price,
            subtotal=subtotal
        )

        product.stock_quantity -= quantity

        db.session.add(order_item)
        db.session.commit()

        return order_item, "Order item created successfully"

    @staticmethod
    def delete_order_item(order_item):

        product = Product.query.get(order_item.product_id)

        if product:
            product.stock_quantity += order_item.quantity

        db.session.delete(order_item)
        db.session.commit()

        return True, "Order item deleted successfully"