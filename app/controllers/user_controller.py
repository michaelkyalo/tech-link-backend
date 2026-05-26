from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.services.user_service import UserService

class UserListResource(Resource):
    @jwt_required()
    def get(self):
        users = UserService.get_users()
        return {
            "success": True,
            "users": [
                {
                    "id": user.user_id,
                    "username": user.full_name,
                    "email": user.email,
                    "role": user.role
                }
                for user in users
            ]
        }, 200

class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = UserService.get_single_user(user_id)
        if not user:
            return {
                "success": False,
                "message": "User not found"
            }, 404
        return {
            "success": True,
            "user": {
                "id": user.user_id,
                "username": user.full_name,
                "email": user.email,
                "role": user.role
            }
        }, 200

class UserRoleResource(Resource):
    @jwt_required()
    def get(self, role):
        users = UserService.get_users_by_role(role)
        return {
            "success": True,
            "users": [
                {
                    "id": user.user_id,
                    "username": user.full_name,
                    "email": user.email
                }
                for user in users
            ]
        }, 200