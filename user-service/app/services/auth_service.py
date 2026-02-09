from app import db
from app.models.user import User

def register_user(username, email, password):
    if User.query.filter_by(email=email).first():
        return None, "User already exists"

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user, None


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return None
    return user

