from flask import Flask

from app.config.config import Config
from app.config.database import db
from app.config.jwt_config import jwt

from app.extensions import (
    bcrypt,
    cors,
    migrate,
    socketio,
    api
)

from app.middleware.error_handler import register_error_handlers

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    api.init_app(app)
    register_error_handlers(app)

    from app.routes.auth_routes import initialize_auth_routes
    from app.routes.product_routes import initialize_product_routes
    from app.routes.order_routes import initialize_order_routes
    from app.routes.user_routes import initialize_user_routes
    from app.routes.chat_routes import initialize_chat_routes
    from app.routes.notification_routes import initialize_notification_routes
    from app.routes.order_item_routes import initialize_order_item_routes
    from app.routes.payment_routes import initialize_payment_routes
    from app.routes.review_routes import initialize_review_routes

    initialize_auth_routes(api)
    initialize_product_routes(api)
    initialize_order_routes(api)
    initialize_user_routes(api)
    initialize_chat_routes(api)
    initialize_notification_routes(api)
    initialize_order_item_routes(api)
    initialize_payment_routes(api)
    initialize_review_routes(api)
    
    return app