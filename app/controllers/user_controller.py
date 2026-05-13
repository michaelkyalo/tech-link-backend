from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.user_service import (
    get_users,
    get_single_user,
    get_users_by_role
)


class UserListResource(Resource):

    @jwt_required()
    def get(self):

        # Fetch all users
        users = get_users()

        return {
            "success": True,
            "users": [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                }
                for user in users
            ]
        },


class UserResource(Resource):

    @jwt_required()
    def get(self, user_id):

        # Find user
        user = get_single_user(user_id)

        if not user:
            return {
                "success": False,
                "message": "User not found"
            }, 

        return {
            "success": True,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        },


class UserRoleResource(Resource):

    @jwt_required()
    def get(self, role):

        # Fetch users by role
        users = get_users_by_role(role)

        return {
            "success": True,
            "users": [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
                for user in users
            ]
        },