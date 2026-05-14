from app.controllers.user_controller import (
    UserListResource,
    UserResource
)


def register_user_routes(api):

    api.add_resource(
        UserListResource,
        "/api/users"
    )

    api.add_resource(
        UserResource,
        "/api/users/<int:user_id>"
    )