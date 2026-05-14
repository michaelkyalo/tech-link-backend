from app.controllers.chat_controller import (
    ChatListResource
)


def register_chat_routes(api):

    api.add_resource(
        ChatListResource,
        "/api/chats"
    )