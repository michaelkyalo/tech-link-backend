from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from app.services.auth_service import (
    register_user,
    login_user
)


class RegisterResource(Resource):

    def post(self):

        
        data = request.get_json()

        
        user, error = register_user(data)

        
        if error:
            return {
                "success": False,
                "message": error
            }, 

        
        token = create_access_token(identity=user.id)

        return {
            "success": True,
            "message": "User registered successfully",
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }, 


class LoginResource(Resource):

    def post(self):

        
        data = request.get_json()

    
        user, error = login_user(data)

        
        if error:
            return {
                "success": False,
                "message": error
            },

    
        token = create_access_token(identity=user.id)

        return {
            "success": True,
            "message": "Login successful",
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        },