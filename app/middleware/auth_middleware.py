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
            return jsonify({"message": "Token is missing"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            # Support multiple possible key names for the user id in the JWT payload
            user_id = data.get("user_id") or data.get("id") or data.get("sub")
            if not user_id:
                return jsonify({"message": "Invalid token payload"}), 401
            current_user = User.query.get(user_id)
            if not current_user:
                return jsonify({"message": "User not found"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401
        return f(*args, current_user=current_user, **kwargs)
    return decorated