from flask import Blueprint, request, jsonify
from app.services.review_service import (
    create_review,
    get_product_reviews,
    delete_review
)

review_bp = Blueprint("review_bp", _name_)


@review_bp.route("/reviews", methods=["POST"])
def add_review():
    data = request.get_json()
    review, error = create_review(data)

    if error:
        return jsonify({"message": error}),

    return jsonify({"message": "Review created", "review": review}),


@review_bp.route("/reviews/<int:product_id>", methods=["GET"])
def fetch_reviews(product_id):
    reviews = get_product_reviews(product_id)
    return jsonify(reviews), 200


@review_bp.route("/reviews/<int:review_id>", methods=["DELETE"])
def remove_review(review_id):
    success, error = delete_review(review_id)

    if error:
        return jsonify({"message": error}),

    return jsonify({"message": "Review deleted"}),