from app.controllers.notification_controller import (
    NotificationListResource
)


def register_notification_routes(api):

    api.add_resource(
        NotificationListResource,
        "/api/notifications"
    )