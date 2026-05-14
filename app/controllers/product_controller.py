from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.product_service import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product
)


class ProductListResource(Resource):

    def get(self):

        
        products = get_all_products()

        return {
            "success": True,
            "products": [
                {
                    "id": product.id,
                    "title": product.title,
                    "description": product.description,
                    "price": product.price,
                    "stock": product.stock,
                    "image_url": product.image_url
                }
                for product in products
            ]
        },

    @jwt_required()
    def post(self):

        
        data = request.get_json()

        
        product = create_product(data)

        return {
            "success": True,
            "message": "Product created successfully",
            "product": {
                "id": product.id,
                "title": product.title
            }
        },


class ProductResource(Resource):

    def get(self, product_id):

        
        product = get_product_by_id(product_id)

        if not product:
            return {
                "success": False,
                "message": "Product not found"
            },

        return {
            "success": True,
            "product": {
                "id": product.id,
                "title": product.title,
                "description": product.description,
                "price": product.price,
                "stock": product.stock,
                "image_url": product.image_url
            }
        },

    @jwt_required()
    def put(self, product_id):

        # Find existing product
        product = get_product_by_id(product_id)

        if not product:
            return {
                "success": False,
                "message": "Product not found"
            },

        
        data = request.get_json()

    
        updated_product = update_product(product, data)

        return {
            "success": True,
            "message": "Product updated successfully",
            "product": {
                "id": updated_product.id,
                "title": updated_product.title
            }
        },

    @jwt_required()
    def delete(self, product_id):

        
        product = get_product_by_id(product_id)

        if not product:
            return {
                "success": False,
                "message": "Product not found"
            }, 

    
        delete_product(product)

        return {
            "success": True,
            "message": "Product deleted successfully"
        },