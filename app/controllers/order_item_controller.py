from flask_restful import Resource
from flask import request
from app.services.order_item_service import OrderItemService
from app.models.order_item_model import OrderItem


class OrderItemListResource(Resource):

    def post(self):
        data = request.get_json()

        item, error = OrderItemService.create_order_item(data)

        if error:
            return {"message": error}, 400

        return {
            "message": "Item added",
            "item": {
                "id": item.id,
                "order_id": item.order_id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "subtotal": item.subtotal
            }
        }, 201


class OrderItemResource(Resource):

    def delete(self, order_item_id):

        order_item = OrderItem.query.get(order_item_id)

        if not order_item:
            return {"message": "Order item not found"}, 404

        success, error = OrderItemService.delete_order_item(order_item)

        if error:
            return {"message": error}, 400

        return {"message": "Item removed"}, 200