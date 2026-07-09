from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.database.db import db
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    CORS(app)

    # Initialize extensions
    db.init_app(app)
    JWTManager(app)

    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register blueprints
    from backend.routes.auth_routes import auth_bp
    from backend.routes.job_routes import job_bp
    from backend.routes.application_routes import application_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(job_bp, url_prefix='/api/jobs')
    app.register_blueprint(application_bp, url_prefix='/api/applications')

    @app.route('/api/health')
    def health():
        return {'status': 'ok'}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
