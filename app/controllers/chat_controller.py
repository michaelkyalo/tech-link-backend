from flask import request, jsonify
from flask_restful import Resource
from app.services.chat_service import ChatService
from app.middleware.auth_middleware import token_required


# ── 1. GET /api/chats/conversations ────────────────────────────────────────
class ConversationListResource(Resource):

    @token_required
    def get(self, current_user=None):
        conversations = ChatService.get_conversations(current_user.user_id)
        return {
            "success": True,
            "conversations": conversations,
        }, 200


# ── 2. POST /api/chats/conversations/start ─────────────────────────────────
class StartConversationResource(Resource):

    @token_required
    def post(self, current_user=None):
        data = request.get_json()
        partner_id = data.get("participantId")
        if not partner_id:
            return {"success": False, "message": "participantId is required"}, 400
        conversation = ChatService.start_conversation(current_user.user_id, partner_id)

        if not conversation:
            return {"success": False, "message": "User not found"}, 404

        return {"success": True, "conversation": conversation}, 200


# ── 3. GET /api/chats/conversations/<partner_id>/messages ──────────────────
class ConversationMessagesResource(Resource):

    @token_required
    def get(self, current_user=None, partner_id=None):
        messages = ChatService.get_messages_for_conversation(current_user.user_id, partner_id)
        return {"success": True, "messages": messages}, 200


# ── 4. POST /api/chats/conversations/<partner_id>/messages ─────────────────
class SendMessageResource(Resource):

    @token_required
    def post(self, current_user=None, partner_id=None):
        data = request.get_json()
        text = data.get("text", "").strip()
        if not text:
            return {"success": False, "message": "text is required"}, 400
        message_data = {
            "sender_id": current_user.user_id,
            "receiver_id": partner_id,
            "message_content": text,
            "product_id": data.get("product_id"),
        }
        message = ChatService.create_message(message_data)
        return {
            "success": True,
            "message": {
                "id": message.message_id,
                "conversationId": partner_id,
                "senderId": message.sender_id,
                "senderName": current_user.full_name,
                "text": message.message_content,
                "createdAt": message.sent_at.isoformat(),
            },
        }, 201


# ── 5. PATCH /api/chats/conversations/<partner_id>/read ───────────────────
class MarkReadResource(Resource):

    @token_required
    def patch(self, current_user=None, partner_id=None):
        return {"success": True, "message": "Marked as read"}, 200


# ── Legacy ─────────────────────────────────────────────────────────────────
class ChatListResource(Resource):

    @token_required
    def post(self, current_user=None):
        data = request.get_json()
        data["sender_id"] = current_user.user_id
        message = ChatService.create_message(data)
        return {
            "success": True,
            "message": "Message sent successfully",
            "chat": {
                "id": message.message_id,
                "sender_id": message.sender_id,
                "receiver_id": message.receiver_id,
                "message_content": message.message_content,
            },
        }, 201

    @token_required
    def get(self, current_user=None):
        receiver_id = request.args.get("receiver_id", type=int)
        chats = ChatService.get_chat_between_users(current_user.user_id, receiver_id)
        return {
            "success": True,
            "messages": [
                {
                    "id": chat.message_id,
                    "sender_id": chat.sender_id,
                    "receiver_id": chat.receiver_id,
                    "message_content": chat.message_content,
                }
                for chat in chats
            ],
        }, 200