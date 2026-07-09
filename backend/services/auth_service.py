# auth_service.py
# Placeholder for authentication-related business logic

from backend.models.user_model import User
from backend.database.db import db
from backend.utils.password_utils import hash_password, check_password

def create_user(name, email, password):
    user = User(name=name, email=email, password=hash_password(password))
    db.session.add(user)
    db.session.commit()
    return user
