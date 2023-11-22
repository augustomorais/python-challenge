from flask import Flask, jsonify
from .utils.database import db
from .routes.warehouse_routes import warehouse_blueprint
from .routes.customer_routes import customer_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@db:5432/database_name'
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Health Check Route
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({'status': 'healthy', 'message': 'API is up and running!'}), 200

    app.register_blueprint(warehouse_blueprint)
    app.register_blueprint(customer_blueprint)

    return app
