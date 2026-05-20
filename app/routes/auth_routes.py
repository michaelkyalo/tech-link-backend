from app.controllers import auth_controller 
from app.controllers.auth_controller import (
    RegisterResource,
    LoginResource
)


def register_auth_routes(api):

    api.add_resource(
        RegisterResource,
        "/api/auth/register"
    )

    api.add_resource(
        LoginResource,
        "/api/auth/login"
    )