from datetime import datetime

from app.config.database import db


class Message(db.Model):

    __tablename__ = "messages"

    message_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    sender_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    receiver_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    product_id = db.Column(
        db.BigInteger,
        db.ForeignKey("products.product_id")
    )

    message_content = db.Column(
        db.Text,
        nullable=False
    )

    sent_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Message {self.message_id}>"