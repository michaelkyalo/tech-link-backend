from app.controllers.review_controller import (
    ReviewListResource,
    ReviewResource
)


def register_review_routes(api):

    api.add_resource(
        ReviewListResource,
        "/api/reviews"
    )

    api.add_resource(
        ReviewResource,
        "/api/reviews/<int:review_id>"
    )