from app.config.database import db


class OrderItem(db.Model):

    __tablename__ = "order_items"

    order_item_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    order_id = db.Column(
        db.BigInteger,
        db.ForeignKey("orders.order_id"),
        nullable=False
    )

    product_id = db.Column(
        db.BigInteger,
        db.ForeignKey("products.product_id"),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    unit_price = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    subtotal = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    def __repr__(self):
        return f"<OrderItem {self.order_item_id}>"