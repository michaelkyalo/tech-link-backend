from datetime import datetime

from app.config.database import db


class Review(db.Model):

    __tablename__ = "reviews"

    review_id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    buyer_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    farmer_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    rating = db.Column(
        db.BigInteger,
        nullable=False
    )

    comment = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Review {self.review_id}>"