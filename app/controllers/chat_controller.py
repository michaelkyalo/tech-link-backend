from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.chat_service import ChatService
from app.models.chat_model import Message



class ChatListResource(Resource):

    @jwt_required()
    def post(self):

        sender_id = get_jwt_identity()
        data = request.get_json()

        data["sender_id"] = sender_id

        message = ChatService.create_message(data)

        return {
            "success": True,
            "message": "Message sent successfully",
            "chat": {
                "id": message.id,
                "sender_id": message.sender_id,
                "receiver_id": message.receiver_id,
                "message_content": message.message_content
            }
        }, 201
class ChatResource(Resource):

    @jwt_required()
    def get(self):

        sender_id = get_jwt_identity()

        receiver_id = request.args.get("receiver_id", type=int)

        chats = ChatService.get_chat_between_users(sender_id, receiver_id)

        return {
            "success": True,
            "messages": [
                {
                    "id": chat.id,
                    "sender_id": chat.sender_id,
                    "receiver_id": chat.receiver_id,
                    "message_content": chat.message_content
                }
                for chat in chats
            ]
        }, 200