from flask import request

from flask_restful import Resource

from flask_jwt_extended import create_access_token

from app.services.auth_service import create_user

from app.schemas.user_schema import UserSchema

user_schema = UserSchema()

class RegisterResource(Resource):

    def post(self):

        data = request.get_json()

        user = create_user(data)

        token = create_access_token(
            identity=user.id
        )

        return {
            "success": True,
            "message": "User registered successfully",
            "token": token,
            "user": user_schema.dump(user)
        }, 201