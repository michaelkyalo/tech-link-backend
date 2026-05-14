from flask import request
from flask_restful import Resource

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.services.chat_service import (
    create_message,
    get_chat_between_users
)


class ChatResource(Resource):

    @jwt_required()
    def post(self):

        
        sender_id = get_jwt_identity()

        
        data = request.get_json()

        
        data["sender_id"] = sender_id

        # Create message
        message = create_message(data)

        return {
            "success": True,
            "message": "Message sent successfully",
            "chat": {
                "id": message.id,
                "message": message.message
            }
        }, 

    @jwt_required()
    def get(self):

        # Get logged-in user
        sender_id = get_jwt_identity()

        
        receiver_id = request.args.get(
            "receiver_id",
            type=int
        )

    
        chats = get_chat_between_users(
            sender_id,
            receiver_id
        )

        return {
            "success": True,
            "messages": [
                {
                    "id": chat.id,
                    "sender_id": chat.sender_id,
                    "receiver_id": chat.receiver_id,
                    "message": chat.message
                }
                for chat in chats
            ]
        }, 