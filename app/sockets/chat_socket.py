from flask_socketio import emit, join_room, leave_room

from app.sockets import socketio


@socketio.on("join_chat")
def handle_join_chat(data):

    room = data["room"]

    join_room(room)

    emit(
        "user_joined",
        {
            "message": f"User joined room {room}"
        },
        room=room
    )


@socketio.on("leave_chat")
def handle_leave_chat(data):

    room = data["room"]

    leave_room(room)

    emit(
        "user_left",
        {
            "message": f"User left room {room}"
        },
        room=room
    )


@socketio.on("send_message")
def handle_send_message(data):

    room = data["room"]

    emit(
        "receive_message",
        {
            "sender_id": data["sender_id"],
            "receiver_id": data["receiver_id"],
            "message": data["message"]
        },
        room=room
    )