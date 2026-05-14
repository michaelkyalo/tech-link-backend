from app.controllers.payment_controller import (
    PaymentListResource,
    PaymentResource
)


def register_payment_routes(api):

    api.add_resource(
        PaymentListResource,
        "/api/payments"
    )

    api.add_resource(
        PaymentResource,
        "/api/payments/<int:payment_id>"
    )