from app.config.database import db
from app.models.order_item_model import OrderItem
from app.models.order_model import Order
from app.models.product_model import Product


class OrderItemService:

    @staticmethod
    def create_order_item(data):
        """
        Create a new order item and calculate subtotal.
        """

        # Validate order exists
        order = Order.query.get(data["order_id"])
        if not order:
            return None, "Order not found"

        # Validate product exists
        product = Product.query.get(data["product_id"])
        if not product:
            return None, "Product not found"

        # Check stock availability
        if product.stock_quantity < data["quantity"]:
            return None, "Insufficient stock"

        unit_price = product.price
        quantity = data["quantity"]
        subtotal = unit_price * quantity

        order_item = OrderItem(
            order_id=data["order_id"],
            product_id=data["product_id"],
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal
        )

        # Reduce stock
        product.stock_quantity -= quantity

        db.session.add(order_item)
        db.session.commit()

        return order_item, "Order item created successfully"

    @staticmethod
    def get_order_item_by_id(order_item_id):
        return OrderItem.query.get(order_item_id)

    @staticmethod
    def get_order_items_by_order(order_id, page=1, per_page=10):
        return OrderItem.query.filter_by(order_id=order_id).paginate(
            page=page,
            per_page=per_page
        )

    @staticmethod
    def delete_order_item(order_item):
        """
        Restore stock when deleting order item.
        """

        product = Product.query.get(order_item.product_id)

        if product:
            product.stock_quantity += order_item.quantity

        db.session.delete(order_item)
        db.session.commit()

        return True, "Order item deleted successfully"