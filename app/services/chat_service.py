from app.config.database import db
from app.models.chat_model import Message

class ChatService:

    @staticmethod
    def create_message(data):
        

        message = Message(
            sender_id=data["sender_id"],
            receiver_id=data["receiver_id"],
            product_id=data["product_id"],
            message_content=data["message"]
        )

        db.session.add(message)
        db.session.commit()

        return message

    @staticmethod
    def get_chat_between_users(sender_id, receiver_id):

        return Message.query.filter(
            (
                (Message.sender_id == sender_id) &
                (Message.receiver_id == receiver_id)
            ) |
            (
                (Message.sender_id == receiver_id) &
                (Message.receiver_id == sender_id)
            )
        ).all()

    @staticmethod
    def delete_message(message):

        db.session.delete(message)
        db.session.commit()

        return True