from app import db
from app.models.cart import Cart
from app.models.order import Order

def add_to_cart(user_id, product_id, quantity):
    cart_item = Cart(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity
    )
    db.session.add(cart_item)
    db.session.commit()
    return cart_item


def get_cart_items(user_id):
    return Cart.query.filter_by(user_id=user_id).all()


def place_order(user_id, total_amount):
    order = Order(
        user_id=user_id,
        total_amount=total_amount
    )
    db.session.add(order)

    Cart.query.filter_by(user_id=user_id).delete()
    db.session.commit()

    return order


def get_orders(user_id):
    return Order.query.filter_by(user_id=user_id).all()

