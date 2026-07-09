from flask_jwt_extended import create_access_token

# Simple helpers (can be expanded)

def create_token(identity):
    return create_access_token(identity=identity)
