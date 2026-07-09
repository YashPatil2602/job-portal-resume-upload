import os
from flask import Blueprint, request, current_app, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from backend.database.db import db
from backend.models.application_model import Application
from backend.models.job_model import Job
from backend.models.user_model import User
from flask_jwt_extended import jwt_required, get_jwt_identity

ALLOWED_EXTENSIONS = {'pdf'}

application_bp = Blueprint('applications', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application_bp.route('/apply', methods=['POST'])
@jwt_required()
def apply_job():
    identity = get_jwt_identity()
    user_id = identity.get('id')

    if 'job_id' not in request.form:
        return jsonify({'msg': 'job_id is required in form data'}), 400
    job_id = request.form.get('job_id')
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'msg': 'Job not found'}), 404

    if 'resume' not in request.files:
        return jsonify({'msg': 'Resume file is required'}), 400
    file = request.files['resume']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'msg': 'Valid PDF required'}), 400

    filename = secure_filename(f"{user_id}_{job_id}_{file.filename}")
    save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(save_path)

    application = Application(user_id=user_id, job_id=job_id, resume_path=save_path)
    db.session.add(application)
    db.session.commit()

    return jsonify({'msg': 'Application submitted', 'application': application.to_dict()}), 201

@application_bp.route('/resume/<int:application_id>', methods=['GET'])
@jwt_required()
def download_resume(application_id):
    # Admin or owner can download
    application = Application.query.get_or_404(application_id)
    identity = get_jwt_identity()
    if identity.get('role') != 'admin' and identity.get('id') != application.user_id:
        return jsonify({'msg': 'Not allowed'}), 403

    folder, filename = os.path.split(application.resume_path)
    return send_from_directory(folder, filename, as_attachment=True)
