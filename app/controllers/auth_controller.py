from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from app.services.auth_service import AuthService



class RegisterResource(Resource):

    def post(self):

        data = request.get_json()

        
        user, error = AuthService.register_user(data)

        
        if error:
            return {
                "success": False,
                "message": error
            }, 400

        
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
        }, 201


class LoginResource(Resource):

    def post(self):

        
        data = request.get_json()

    
        user, error = AuthService.login_user(data)

        
        if error:
            return {
                "success": False,
                "message": error
            },401

    
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
        },200