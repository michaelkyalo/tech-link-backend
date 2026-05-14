from app.config.database import db


class Farmer(db.Model):

    __tablename__ = "farmers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    farm_name = db.Column(
        db.String(120),
        nullable=False
    )

    farm_location = db.Column(
        db.String(255),
        nullable=False
    )

    farm_description = db.Column(
        db.Text
    )

    def __repr__(self):

        return f"<Farmer {self.farm_name}>"