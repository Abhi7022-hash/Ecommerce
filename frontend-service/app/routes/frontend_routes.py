import os
from flask import Blueprint, render_template, request, redirect, url_for, session
import requests

frontend_bp = Blueprint("frontend", __name__)

USER_SERVICE = os.getenv("USER_SERVICE_URL") + "/api/users"
PRODUCT_SERVICE = os.getenv("PRODUCT_SERVICE_URL") + "/api/products"
ORDER_SERVICE = os.getenv("ORDER_SERVICE_URL") + "/api/orders"



@frontend_bp.route("/")
def index():
    return render_template("index.html")


@frontend_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        requests.post(f"{USER_SERVICE}/register", json={
            "username": request.form["username"],
            "email": request.form["email"],
            "password": request.form["password"]
        })
        return redirect(url_for("frontend.login"))
    return render_template("register.html")


@frontend_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        resp = requests.post(f"{USER_SERVICE}/login", json={
            "email": request.form["email"],
            "password": request.form["password"]
        })
        if resp.status_code == 200:
            session["token"] = resp.json()["access_token"]
            return redirect(url_for("frontend.products"))
    return render_template("login.html")


@frontend_bp.route("/products")
def products():
    products = requests.get(PRODUCT_SERVICE).json()
    return render_template("products.html", products=products)


@frontend_bp.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    token = session.get("token")
    headers = {"Authorization": f"Bearer {token}"}

    requests.post(
        f"{ORDER_SERVICE}/cart",
        json={"product_id": product_id, "quantity": 1},
        headers=headers
    )
    return redirect(url_for("frontend.products"))


@frontend_bp.route("/cart")
def cart():
    token = session.get("token")
    headers = {"Authorization": f"Bearer {token}"}

    items = requests.get(f"{ORDER_SERVICE}/cart", headers=headers).json()
    return render_template("cart.html", items=items)

