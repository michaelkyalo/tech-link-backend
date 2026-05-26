from app.config.database import db
from app.models.chat_model import Message
from app.models.user_model import User
from sqlalchemy import or_, and_


class ChatService:

    # ── Send a message ──────────────────────────────────────────────────────
    @staticmethod
    def create_message(data):
        message = Message(
            sender_id=data["sender_id"],
            receiver_id=data["receiver_id"],
            product_id=data.get("product_id"),
            message_content=data["message_content"],
        )
        db.session.add(message)
        db.session.commit()
        return message

    # ── Get all messages between two users ─────────────────────────────────
    @staticmethod
    def get_chat_between_users(user_a_id, user_b_id):
        return (
            Message.query
            .filter(
                or_(
                    and_(Message.sender_id == user_a_id, Message.receiver_id == user_b_id),
                    and_(Message.sender_id == user_b_id, Message.receiver_id == user_a_id),
                )
            )
            .order_by(Message.sent_at.asc())
            .all()
        )

    # ── Get all conversations for a user ───────────────────────────────────
    @staticmethod
    def get_conversations(current_user_id):
        sent_to = (
            db.session.query(Message.receiver_id.label("partner_id"))
            .filter(Message.sender_id == current_user_id)
        )
        received_from = (
            db.session.query(Message.sender_id.label("partner_id"))
            .filter(Message.receiver_id == current_user_id)
        )
        partner_ids = {row.partner_id for row in sent_to.union(received_from).all()}

        conversations = []
        for partner_id in partner_ids:
            partner = User.query.get(partner_id)
            if not partner:
                continue

            last_msg = (
                Message.query
                .filter(
                    or_(
                        and_(Message.sender_id == current_user_id, Message.receiver_id == partner_id),
                        and_(Message.sender_id == partner_id,      Message.receiver_id == current_user_id),
                    )
                )
                .order_by(Message.sent_at.desc())
                .first()
            )

            unread_count = (
                Message.query
                .filter(
                    Message.sender_id == partner_id,
                    Message.receiver_id == current_user_id,
                )
                .count()
            )

            conversations.append({
                "id": partner_id,
                "participantId": partner_id,
                "participantName": partner.full_name,
                "participantRole": partner.role,
                "participantLocation": partner.location,
                "lastMessage": last_msg.message_content if last_msg else None,
                "unreadCount": unread_count,
                "updatedAt": last_msg.sent_at.isoformat() if last_msg else None,
            })

        conversations.sort(key=lambda c: c["updatedAt"] or "", reverse=True)
        return conversations

    # ── Get messages for a conversation ────────────────────────────────────
    @staticmethod
    def get_messages_for_conversation(current_user_id, partner_id):
        messages = (
            Message.query
            .filter(
                or_(
                    and_(Message.sender_id == current_user_id, Message.receiver_id == partner_id),
                    and_(Message.sender_id == partner_id,      Message.receiver_id == current_user_id),
                )
            )
            .order_by(Message.sent_at.asc())
            .all()
        )

        result = []
        for m in messages:
            sender = User.query.get(m.sender_id)
            result.append({
                "id": m.message_id,
                "conversationId": partner_id,
                "senderId": m.sender_id,
                "senderName": sender.full_name if sender else "Unknown",
                "text": m.message_content,
                "createdAt": m.sent_at.isoformat(),
            })
        return result

    # ── Start or get a conversation with a user ────────────────────────────
    @staticmethod
    def start_conversation(current_user_id, partner_id):
        partner = User.query.get(partner_id)
        if not partner:
            return None

        last_msg = (
            Message.query
            .filter(
                or_(
                    and_(Message.sender_id == current_user_id, Message.receiver_id == partner_id),
                    and_(Message.sender_id == partner_id,      Message.receiver_id == current_user_id),
                )
            )
            .order_by(Message.sent_at.desc())
            .first()
        )

        return {
            "id": partner_id,
            "participantId": partner_id,
            "participantName": partner.full_name,
            "participantRole": partner.role,
            "participantLocation": partner.location,
            "lastMessage": last_msg.message_content if last_msg else None,
            "unreadCount": 0,
            "updatedAt": last_msg.sent_at.isoformat() if last_msg else None,
        }