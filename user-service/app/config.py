class Config:
    SECRET_KEY = "user-service-secret"
    JWT_SECRET_KEY = "jwt-user-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

