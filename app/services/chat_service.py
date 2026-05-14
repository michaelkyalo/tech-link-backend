from app.config.database import db
from app.models.chat_model import Chat


def create_message(data):
    message = Chat(
        sender_id=data["sender_id"],
        receiver_id=data["receiver_id"],
        message=data["message"]
    )

    db.session.add(message)
    db.session.commit()
    return message


def get_chat_between_users(sender_id, receiver_id):
    return Chat.query.filter(
        (
            (Chat.sender_id == sender_id) &
            (Chat.receiver_id == receiver_id)
        ) |
        (
            (Chat.sender_id == receiver_id) &
            (Chat.receiver_id == sender_id)
        )
    ).all()


def delete_message(message):
    db.session.delete(message)
    db.session.commit()
    return True