from app.controllers.chat_controller import (
    ChatListResource,
    ConversationListResource,
    StartConversationResource,
    ConversationMessagesResource,
    SendMessageResource,
    MarkReadResource,
)


def register_chat_routes(api):

    # ── Legacy route (kept as-is) ──────────────────────────────────────────
    api.add_resource(ChatListResource, "/api/chats")

    # ── New conversation routes ────────────────────────────────────────────

    # GET  /api/chats/conversations        → list all threads for current user
    # POST /api/chats/conversations        → start/get a conversation
    api.add_resource(
        ConversationListResource,
        "/api/chats/conversations",
        endpoint="conversation_list",
    )

    api.add_resource(
        StartConversationResource,
        "/api/chats/conversations/start",
        endpoint="start_conversation",
    )

    # GET  /api/chats/conversations/<partner_id>/messages  → get messages
    # POST /api/chats/conversations/<partner_id>/messages  → send a message
    api.add_resource(
        ConversationMessagesResource,
        "/api/chats/conversations/<int:partner_id>/messages",
        endpoint="conversation_messages_get",
    )

    api.add_resource(
        SendMessageResource,
        "/api/chats/conversations/<int:partner_id>/messages",
        endpoint="conversation_messages_post",
    )

    # PATCH /api/chats/conversations/<partner_id>/read  → mark as read
    api.add_resource(
        MarkReadResource,
        "/api/chats/conversations/<int:partner_id>/read",
        endpoint="mark_read",
    )