from app.models.user_model import User


def get_users():
    return User.query.all()


def get_single_user(user_id):
    return User.query.get(user_id)


def get_users_by_role(role):
    return User.query.filter_by(role=role).all()