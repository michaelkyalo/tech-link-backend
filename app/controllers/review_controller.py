from flask_restful import Resource
from flask import request
from app.services.review_service import ReviewService


class ReviewListResource(Resource):
    def get(self):
        reviews = ReviewService.get_all_reviews()

        return [
            {
                "id": r.id,
                "user_id": r.user_id,
                "product_id": r.product_id,
                "rating": r.rating,
                "comment": r.comment
            }
            for r in reviews.items
        ], 200

    def post(self):
        data = request.get_json()

        review, error = ReviewService.create_review(data)

        if error:
            return {"message": error}, 400

        return {"message": "Review created"}, 201


class ReviewResource(Resource):

    def get(self, review_id):
        review = ReviewService.get_review_by_id(review_id)

        if not review:
            return {"message": "Not found"}, 404

        return {
            "id": review.id,
            "rating": review.rating,
            "comment": review.comment
        }, 200

    def delete(self, review_id):
        review = ReviewService.get_review_by_id(review_id)

        if not review:
            return {"message": "Not found"}, 404

        ReviewService.delete_review(review)

        return {"message": "Deleted"}, 200