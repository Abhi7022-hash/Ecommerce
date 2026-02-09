from flask import Flask
from app.config import Config
from app import db, jwt
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(user_bp, url_prefix="/api/users")

    with app.app_context():
        db.create_all()

    return app

