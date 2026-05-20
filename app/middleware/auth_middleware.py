from functools import wraps
from flask import request, jsonify
import jwt
import os
from app.models.user_model import User


SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing"})

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.get(data["user_id"])

            if not current_user:
                return jsonify({"message": "User not found"})

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired"})

        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"})

        return f(current_user, *args, **kwargs)

    return decorated