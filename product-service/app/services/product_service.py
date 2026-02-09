from app import db
from app.models.product import Product
from app.models.category import Category

def create_category(name):
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return category


def create_product(name, description, price, category_id):
    product = Product(
        name=name,
        description=description,
        price=price,
        category_id=category_id
    )
    db.session.add(product)
    db.session.commit()
    return product


def get_all_products():
    return Product.query.all()


def get_product_by_id(product_id):
    return Product.query.get(product_id)

