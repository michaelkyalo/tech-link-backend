from app.config.database import db
from app.models.review_model import Review
from app.models.user_model import User
from app.models.product_model import Product


class ReviewService:

    @staticmethod
    def create_review(data):
        """
        Create a product review by a user.
        """

        user = User.query.get(data["user_id"])
        if not user:
            return None, "User not found"

        product = Product.query.get(data["product_id"])
        if not product:
            return None, "Product not found"

        if data["rating"] < 1 or data["rating"] > 5:
            return None, "Rating must be between 1 and 5"

        review = Review(
            user_id=data["user_id"],
            product_id=data["product_id"],
            rating=data["rating"],
            comment=data.get("comment")
        )

        db.session.add(review)
        db.session.commit()

        return review, "Review created successfully"

    @staticmethod
    def get_review_by_id(review_id):
        return Review.query.get(review_id)

    @staticmethod
    def get_all_reviews(page=1, per_page=10):
        return Review.query.paginate(page=page, per_page=per_page)

    @staticmethod
    def delete_review(review):
        db.session.delete(review)
        db.session.commit()

        return True, "Review deleted successfully"