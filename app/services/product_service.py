from app.config.database import db
from app.models.product_model import Product

class ProductService:

    @staticmethod
    def create_product(data, image_url=None):

        product = Product(
            title=data["title"],
            description=data["description"],
            price=data["price"],
            stock=data.get("stock", 0),
            image_url=image_url,
            farmer_id=data["farmer_id"]
        )

        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def get_all_products(page=1, per_page=10):

        return Product.query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def update_product(product, data):

        product.title = data.get("title", product.title)
        product.description = data.get("description", product.description)
        product.price = data.get("price", product.price)
        product.stock = data.get("stock", product.stock)

        db.session.commit()
        return product

    @staticmethod
    def delete_product(product):
        
        db.session.delete(product)
        db.session.commit()
        return True