from app.controllers.order_item_controller import (
    OrderItemListResource,
    OrderItemResource
)


def register_order_item_routes(api):

    api.add_resource(
        OrderItemListResource,
        "/api/order-items"
    )

    api.add_resource(
        OrderItemResource,
        "/api/order-items/<int:order_item_id>"
    )