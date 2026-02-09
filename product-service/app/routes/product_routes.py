from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.product_service import (
    create_category,
    create_product,
    get_all_products,
    get_product_by_id
)

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/category", methods=["POST"])
@jwt_required()
def add_category():
    data = request.get_json()
    category = create_category(data.get("name"))

    return jsonify({
        "id": category.id,
        "name": category.name
    }), 201


@product_bp.route("/", methods=["POST"])
@jwt_required()
def add_product():
    data = request.get_json()
    product = create_product(
        data.get("name"),
        data.get("description"),
        data.get("price"),
        data.get("category_id")
    )

    return jsonify({
        "id": product.id,
        "name": product.name
    }), 201


@product_bp.route("/", methods=["GET"])
def list_products():
    products = get_all_products()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": p.price,
            "category_id": p.category_id
        } for p in products
    ])


@product_bp.route("/<int:product_id>", methods=["GET"])
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "category_id": product.category_id
    })

