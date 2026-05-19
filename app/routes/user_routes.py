from app.controllers.user_controller import (
    UserListResource,
    UserResource,
    UserRoleResource
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
    api.add_resource(
        UserRoleResource, 
        "/api/users/role/<string:role>"
    )