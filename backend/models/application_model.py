from datetime import datetime
from backend.database.db import db

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    resume_path = db.Column(db.String(500), nullable=False)  # store filename only
    status = db.Column(db.String(50), default='pending')
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'job_id': self.job_id,
            'resume_path': self.resume_path,
            'resume_url': f"/api/applications/resume/{self.id}",
            'status': self.status,
            'applied_at': self.applied_at.isoformat()
        }
