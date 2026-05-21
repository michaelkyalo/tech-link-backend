from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.product_service import ProductService
from app.models.user_model import User

def product_to_dict(product):
    return {
        "product_id":   product.product_id,
        "farmer_id":    product.farmer_id,
        "farmer_name":  product.farmer.full_name if product.farmer else None,
        "product_name": product.product_name,
        "description":  product.description,
        "category":     product.category,
        "price":        str(product.price),
        "quantity":     product.quantity,
        "image_url":    product.image_url,
        "location":     product.location,
        "created_at":   str(product.created_at)
    }

class ProductListResource(Resource):
    def get(self):
        page     = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)
        paginated = ProductService.get_all_products(page=page, per_page=per_page)
        return {
            "success":  True,
            "page":     paginated.page,
            "pages":    paginated.pages,
            "total":    paginated.total,
            "products": [product_to_dict(p) for p in paginated.items]
        }

    @jwt_required()
    def post(self):
        current_user_id = int(get_jwt_identity())
        user = User.query.get(current_user_id)
        if not user or user.role != "farmer":
            return {"success": False, "message": "Only farmers can add products"}, 403
        data = request.get_json()
        required = ["product_name", "description", "category", "price"]
        for field in required:
            if not data.get(field):
                return {"success": False, "message": f"{field} is required"}, 400
        product = ProductService.create_product(data, farmer_id=current_user_id)
        return {"success": True, "message": "Product created", "product": product_to_dict(product)}, 201

class ProductResource(Resource):
    def get(self, product_id):
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return {"success": False, "message": "Product not found"}, 404
        return {"success": True, "product": product_to_dict(product)}

    @jwt_required()
    def put(self, product_id):
        current_user_id = int(get_jwt_identity())
        user = User.query.get(current_user_id)
        if not user or user.role != "farmer":
            return {"success": False, "message": "Only farmers can update products"}, 403
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return {"success": False, "message": "Product not found"}, 404
        if product.farmer_id != current_user_id:
            return {"success": False, "message": "You can only edit your own products"}, 403
        data = request.get_json()
        updated = ProductService.update_product(product, data)
        return {"success": True, "message": "Product updated", "product": product_to_dict(updated)}

    @jwt_required()
    def delete(self, product_id):
        current_user_id = int(get_jwt_identity())
        user = User.query.get(current_user_id)
        if not user or user.role != "farmer":
            return {"success": False, "message": "Only farmers can delete products"}, 403
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return {"success": False, "message": "Product not found"}, 404
        if product.farmer_id != current_user_id:
            return {"success": False, "message": "You can only delete your own products"}, 403
        ProductService.delete_product(product)
        return {"success": True, "message": "Product deleted"}