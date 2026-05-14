from app.controllers.delivery_controller import (
    DeliveryListResource,
    DeliveryResource
)


def register_delivery_routes(api):

    api.add_resource(
        DeliveryListResource,
        "/api/deliveries"
    )

    api.add_resource(
        DeliveryResource,
        "/api/deliveries/<int:delivery_id>"
    )