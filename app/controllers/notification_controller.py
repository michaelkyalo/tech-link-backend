from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.notification_service import (
    get_notifications
)


class NotificationListResource(Resource):

    @jwt_required()
    def get(self):

        
        notifications = get_notifications()

        return {
            "success": True,
            "notifications": [
                {
                    "id": notification.id,
                    "title": notification.title,
                    "message": notification.message,
                    "is_read": notification.is_read
                }
                for notification in notifications
            ]
        }, 