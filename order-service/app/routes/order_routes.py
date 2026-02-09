from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.order_service import (
    add_to_cart,
    get_cart_items,
    place_order,
    get_orders
)
from app.utils.jwt_utils import get_user_id

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/cart", methods=["POST"])
@jwt_required()
def add_cart():
    data = request.get_json()
    user_id = get_user_id()

    cart_item = add_to_cart(
        user_id,
        data.get("product_id"),
        data.get("quantity", 1)
    )

    return jsonify({"message": "Item added to cart"}), 201


@order_bp.route("/cart", methods=["GET"])
@jwt_required()
def view_cart():
    user_id = get_user_id()
    items = get_cart_items(user_id)

    return jsonify([
        {
            "product_id": i.product_id,
            "quantity": i.quantity
        } for i in items
    ])


@order_bp.route("/place", methods=["POST"])
@jwt_required()
def order_place():
    user_id = get_user_id()
    data = request.get_json()

    order = place_order(user_id, data.get("total_amount"))
    return jsonify({
        "order_id": order.id,
        "status": order.status
    })


@order_bp.route("/", methods=["GET"])
@jwt_required()
def orders():
    user_id = get_user_id()
    orders = get_orders(user_id)

    return jsonify([
        {
            "order_id": o.id,
            "total_amount": o.total_amount,
            "status": o.status,
            "created_at": o.created_at
        } for o in orders
    ])

