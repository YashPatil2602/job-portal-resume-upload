from backend.app import create_app
from backend.database.db import db
from backend.utils.password_utils import hash_password
from backend.models.user_model import User
import os

app = create_app()

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@jobportal.com')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'adminpass')

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email=ADMIN_EMAIL).first():
        admin = User(name='Admin', email=ADMIN_EMAIL, password=hash_password(ADMIN_PASSWORD), role='admin')
        db.session.add(admin)
        db.session.commit()
        print('Admin user created:', ADMIN_EMAIL)
    else:
        print('Admin user already exists')
