from datetime import datetime

from app.config.database import db


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    full_name = db.Column(
        db.String(120),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        unique=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        nullable=False
    )

    location = db.Column(
        db.String(255)
    )

    profile_image = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    products = db.relationship(
        "Product",
        backref="farmer",
        lazy=True
    )

    notifications = db.relationship(
        "Notification",
        backref="user",
        lazy=True
    )

    def __repr__(self):

        return f"<User {self.full_name}>"