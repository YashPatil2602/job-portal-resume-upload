from flask import Blueprint, request, jsonify
from backend.database.db import db
from backend.models.job_model import Job
from flask_jwt_extended import jwt_required, get_jwt_identity

job_bp = Blueprint('jobs', __name__)

@job_bp.route('/', methods=['GET'])
def list_jobs():
    q = request.args.get('q')
    query = Job.query
    if q:
        like = f"%{q}%"
        query = query.filter((Job.title.ilike(like)) | (Job.company.ilike(like)) | (Job.location.ilike(like)))
    jobs = [j.to_dict() for j in query.order_by(Job.created_at.desc()).all()]
    return jsonify(jobs)

@job_bp.route('/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = Job.query.get_or_404(job_id)
    return jsonify(job.to_dict())

# Protected admin endpoints (simple example)
@job_bp.route('/', methods=['POST'])
@jwt_required()
def create_job():
    identity = get_jwt_identity()
    if identity.get('role') != 'admin':
        return jsonify({'msg': 'Admin only'}), 403

    data = request.get_json() or {}
    job = Job(
        title=data.get('title'),
        company=data.get('company'),
        location=data.get('location'),
        salary=data.get('salary'),
        description=data.get('description'),
        requirements=data.get('requirements')
    )
    db.session.add(job)
    db.session.commit()
    return jsonify(job.to_dict()), 201

@job_bp.route('/<int:job_id>', methods=['PUT'])
@jwt_required()
def update_job(job_id):
    identity = get_jwt_identity()
    if identity.get('role') != 'admin':
        return jsonify({'msg': 'Admin only'}), 403
    job = Job.query.get_or_404(job_id)
    data = request.get_json() or {}
    for key in ('title','company','location','salary','description','requirements'):
        if key in data:
            setattr(job, key, data.get(key))
    db.session.commit()
    return jsonify(job.to_dict())

@job_bp.route('/<int:job_id>', methods=['DELETE'])
@jwt_required()
def delete_job(job_id):
    identity = get_jwt_identity()
    if identity.get('role') != 'admin':
        return jsonify({'msg': 'Admin only'}), 403
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({'msg': 'Deleted'})
