from datetime import datetime

from app.config.database import db


class Product(db.Model):

    __tablename__ = "products"

    product_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    farmer_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    product_name = db.Column(
        db.String(120),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    price = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    quantity = db.Column(
        db.BigInteger,
        default=0
    )

    image_url = db.Column(
        db.String(255)
    )

    location = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    reviews = db.relationship(
        "Review",
        backref="product",
        lazy=True
    )

    def __repr__(self):

        return f"<Product {self.product_name}>"