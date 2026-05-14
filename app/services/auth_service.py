from app.config.database import db
from app.extensions import bcrypt
from app.models.user_model import User


def register_user(data):
    existing_user = User.query.filter(
        (User.email == data["email"]) |
        (User.username == data["username"])
    ).first()

    if existing_user:
        return None, "User already exists"

    hashed_password = bcrypt.generate_password_hash(
        data["password"]
    ).decode("utf-8")

    user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        role=data.get("role", "buyer")
    )

    db.session.add(user)
    db.session.commit()

    return user, None


def login_user(data):
    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return None, "Invalid email or password"

    valid_password = bcrypt.check_password_hash(
        user.password,
        data["password"]
    )

    if not valid_password:
        return None, "Invalid email or password"

    return user, None


def get_all_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def update_user(user, data):
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)

    db.session.commit()
    return user


def delete_user(user):
    db.session.delete(user)
    db.session.commit()
    return True