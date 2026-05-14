from app.controllers.order_controller import (
    OrderListResource,
    OrderResource
)


def register_order_routes(api):

    api.add_resource(
        OrderListResource,
        "/api/orders"
    )

    api.add_resource(
        OrderResource,
        "/api/orders/<int:order_id>"
    )