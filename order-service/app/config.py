class Config:
    SECRET_KEY = "order-service-secret"
    JWT_SECRET_KEY = "jwt-order-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///orders.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

