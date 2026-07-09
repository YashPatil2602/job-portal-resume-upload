# job_service.py
# Placeholder for job-related business logic
from backend.models.job_model import Job
from backend.database.db import db

def create_job(**kwargs):
    job = Job(**kwargs)
    db.session.add(job)
    db.session.commit()
    return job
