# application_service.py
# Placeholder for application-related business logic
from backend.models.application_model import Application
from backend.database.db import db

def create_application(user_id, job_id, resume_path):
    app = Application(user_id=user_id, job_id=job_id, resume_path=resume_path)
    db.session.add(app)
    db.session.commit()
    return app
