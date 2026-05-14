from datetime import datetime

from app.config.database import db


class Notification(db.Model):

    __tablename__ = "notifications"

    notification_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    title = db.Column(
        db.String(120),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    notification_type = db.Column(
        db.String(50)
    )

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Notification {self.notification_id}>"