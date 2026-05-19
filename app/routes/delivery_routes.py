from app.controllers.delivery_controller import (
    DeliveryListResource,
    DeliveryOrderResource,
    DeliveryResource
)


def register_delivery_routes(api):

    api.add_resource(
        DeliveryListResource,
        "/api/deliveries"
    )

    api.add_resource(
        DeliveryOrderResource,
        "/api/deliveries/order/<int:order_id>"
    )

    api.add_resource(
        DeliveryResource,
        "/api/deliveries/<int:delivery_id>"
    )