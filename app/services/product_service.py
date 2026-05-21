from app.config.database import db
from app.models.product_model import Product

class ProductService:

    @staticmethod
    def create_product(data, farmer_id, image_url=None):
        product = Product(
            farmer_id    = farmer_id,
            product_name = data["product_name"],
            description  = data["description"],
            category     = data["category"],
            price        = data["price"],
            quantity     = data.get("quantity", 0),
            image_url    = image_url or data.get("image_url"),
            location     = data.get("location")
        )
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def get_all_products(page=1, per_page=10):
        return Product.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def update_product(product, data):
        product.product_name = data.get("product_name", product.product_name)
        product.description  = data.get("description", product.description)
        product.category     = data.get("category", product.category)
        product.price        = data.get("price", product.price)
        product.quantity     = data.get("quantity", product.quantity)
        product.location     = data.get("location", product.location)
        db.session.commit()
        return product

    @staticmethod
    def delete_product(product):
        db.session.delete(product)
        db.session.commit()
        return True