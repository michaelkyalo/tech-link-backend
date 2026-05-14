from app.config.database import db


class Buyer(db.Model):

    __tablename__ = "buyers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    address = db.Column(
        db.String(255)
    )

    phone_number = db.Column(
        db.String(20)
    )

    def __repr__(self):

        return f"<Buyer {self.user_id}>"