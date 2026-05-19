from flask_restful import Api

from app.routes.auth_routes import register_auth_routes
from app.routes.user_routes import register_user_routes
from app.routes.product_routes import register_product_routes
from app.routes.order_routes import register_order_routes
from app.routes.order_item_routes import register_order_item_routes
from app.routes.payment_routes import register_payment_routes
from app.routes.review_routes import register_review_routes
from app.routes.delivery_routes import register_delivery_routes     
from app.routes.chat_routes import register_chat_routes
from app.routes.notification_routes import register_notification_routes


def register_routes(api):
    

    register_auth_routes(api)
    register_user_routes(api)
    register_product_routes(api)
    register_order_routes(api)
    register_order_item_routes(api)
    register_payment_routes(api)
    register_review_routes(api)
    register_delivery_routes(api)
    register_chat_routes(api)
    register_notification_routes(api)