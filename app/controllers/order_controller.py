from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.order_service import (
    create_order,
    get_all_orders,
    get_order_by_id,
    update_order_status,
    delete_order
)


class OrderListResource(Resource):

    @jwt_required()
    def get(self):

        # Fetch all orders
        orders = get_all_orders()

        return {
            "success": True,
            "orders": [
                {
                    "id": order.id,
                    "buyer_id": order.buyer_id,
                    "total_amount": order.total_amount,
                    "status": order.status
                }
                for order in orders
            ]
        },

    @jwt_required()
    def post(self):

        # Get request data
        data = request.get_json()

        # Create order
        order = create_order(data)

        return {
            "success": True,
            "message": "Order created successfully",
            "order": {
                "id": order.id,
                "status": order.status
            }
        },


class OrderResource(Resource):

    @jwt_required()
    def get(self, order_id):

        # Find order
        order = get_order_by_id(order_id)

        if not order:
            return {
                "success": False,
                "message": "Order not found"
            }, 404

        return {
            "success": True,
            "order": {
                "id": order.id,
                "buyer_id": order.buyer_id,
                "total_amount": order.total_amount,
                "status": order.status
            }
        },

    @jwt_required()
    def put(self, order_id):

        
        order = get_order_by_id(order_id)

        if not order:
            return {
                "success": False,
                "message": "Order not found"
            },

    
        data = request.get_json()

    
        updated_order = update_order_status(order, data)

        return {
            "success": True,
            "message": "Order updated successfully",
            "order": {
                "id": updated_order.id,
                "status": updated_order.status
            }
        },

    @jwt_required()
    def delete(self, order_id):

        
        order = get_order_by_id(order_id)

        if not order:
            return {
                "success": False,
                "message": "Order not found"
            },

        
        delete_order(order)

        return {
            "success": True,
            "message": "Order deleted successfully"
        },