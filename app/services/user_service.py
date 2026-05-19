from app.models.user_model import User
from app.config.database import db
class UserService:

    @staticmethod
    def get_users():
        
        return User.query.all()

    @staticmethod
    def get_single_user(user_id):        
        return User.query.get(user_id)

    @staticmethod
    def get_users_by_role(role):        
        return User.query.filter_by(role=role).all()

    @staticmethod
    def update_user(user, data):

        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user):

        db.session.delete(user)
        db.session.commit()
        return True