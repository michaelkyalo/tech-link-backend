from app.controllers.product_controller import (
    ProductListResource,
    ProductResource
)


def register_product_routes(api):

    api.add_resource(
        ProductListResource,
        "/api/products"
    )

    api.add_resource(
        ProductResource,
        "/api/products/<int:product_id>"
    )