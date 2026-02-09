from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import register_user, authenticate_user
from app.utils.jwt_utils import generate_token
from app.models.user import User

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user, error = register_user(
        data.get("username"),
        data.get("email"),
        data.get("password")
    )

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "User registered successfully"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = authenticate_user(data.get("email"), data.get("password"))

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user.id)
    return jsonify({"access_token": token})


@user_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email
    })

