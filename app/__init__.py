from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import Config
from flask_swagger_ui import get_swaggerui_blueprint
from app.error_handlers import register_error_handlers

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API',
    }
)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from app.routes.auth_routes import auth_bp
    from app.routes.employee_routes import employee_bp
    @app.route("/")
    def home():
        return jsonify({
            "Message":"app up and running successfully"
        })

    app.register_blueprint(auth_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(swagger_ui_blueprint,url_prefix=SWAGGER_URL)
    register_error_handlers(app)
    return app
