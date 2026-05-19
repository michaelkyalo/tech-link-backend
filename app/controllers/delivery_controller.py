from flask_restful import Resource
from flask import request
from app.services.delivery_service import DeliveryService
from app.models.delivery_model import Delivery


class DeliveryListResource(Resource):

    def post(self):
        data = request.get_json()

        delivery, error = DeliveryService.create_delivery(data)

        if error:
            return {"message": error}, 400

        return {
            "message": "Delivery created",
            "delivery": {
                "id": delivery.id,
                "order_id": delivery.order_id,
                "status": delivery.status
            }
        }, 201


class DeliveryOrderResource(Resource):

    def get(self, order_id):

        delivery = DeliveryService.get_delivery_by_order(order_id)

        if not delivery:
            return {"message": "Delivery not found"}, 404

        return {
            "id": delivery.id,
            "order_id": delivery.order_id,
            "status": delivery.status
        }, 200


class DeliveryResource(Resource):

    def patch(self, delivery_id):

        data = request.get_json()

        updated, error = DeliveryService.update_delivery_status(delivery_id, data)

        if error:
            return {"message": error}, 400

        return {
            "message": "Delivery status updated",
            "delivery": {
                "id": updated.id,
                "status": updated.status
            }
        }, 200