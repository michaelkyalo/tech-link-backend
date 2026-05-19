from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.notification_service import NotificationService


class NotificationListResource(Resource):

    @jwt_required()
    def get(self):

        notifications = NotificationService.get_notifications()

        return {
            "success": True,
            "notifications": notifications
        }, 200