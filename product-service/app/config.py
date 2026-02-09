class Config:
    SECRET_KEY = "product-service-secret"
    JWT_SECRET_KEY = "jwt-product-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///products.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

