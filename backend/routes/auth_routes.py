from flask import Blueprint, request, jsonify
from backend.database.db import db
from backend.models.user_model import User
from backend.utils.password_utils import hash_password, check_password
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'msg': 'Missing fields'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'msg': 'Email already registered'}), 400

    user = User(name=name, email=email, password=hash_password(password))
    db.session.add(user)
    db.session.commit()

    return jsonify({'msg': 'User registered', 'user': user.to_dict()}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'msg': 'Missing fields'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not check_password(password, user.password):
        return jsonify({'msg': 'Invalid credentials'}), 401

    access_token = create_access_token(identity={'id': user.id, 'role': user.role})
    return jsonify({'access_token': access_token, 'user': user.to_dict()}), 200
