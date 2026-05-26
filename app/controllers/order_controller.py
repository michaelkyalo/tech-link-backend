from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.order_service import OrderService


def order_to_dict(order):
    """Safe serializer to avoid Decimal JSON errors"""
    return {
        "id": order.order_id,
        "buyer_id": order.buyer_id,
        "total_amount": float(order.total_amount),
        "status": order.status
    }


class OrderListResource(Resource):

    @jwt_required()
    def get(self):

        orders = OrderService.get_all_orders()

        return {
            "success": True,
            "orders": [order_to_dict(order) for order in orders]
        }, 200

    @jwt_required()
    def post(self):

        data = request.get_json()

        order = OrderService.create_order(data)

        return {
            "success": True,
            "message": "Order created successfully",
            "order": order_to_dict(order)
        }, 201


class OrderResource(Resource):

    @jwt_required()
    def get(self, order_id):

        order = OrderService.get_order_by_id(order_id)

        if not order:
            return {
                "success": False,
                "message": "Order not found"
            }, 404

        return {
            "success": True,
            "order": order_to_dict(order)
        }, 200

    @jwt_required()
    def put(self, order_id):

        order = OrderService.get_order_by_id(order_id)

        if not order:
            return {
                "success": False,
                "message": "Order not found"
            }, 404

        data = request.get_json()

        updated_order = OrderService.update_order_status(order, data)

        return {
            "success": True,
            "message": "Order updated successfully",
            "order": order_to_dict(updated_order)
        }, 200

    @jwt_required()
    def delete(self, order_id):

        order = OrderService.get_order_by_id(order_id)

        if not order:
            return {
                "success": False,
                "message": "Order not found"
            }, 404

        OrderService.delete_order(order)

        return {
            "success": True,
            "message": "Order deleted successfully"
        }, 200