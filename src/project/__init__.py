from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from marshmallow.exceptions import ValidationError
from .configs import Config


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def register_blueprint(app):
    from project.endpoints import blueprint as pedidos

    app.register_blueprint(pedidos)


def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def validation_error_handler(e):
        return e.messages, 400

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprint(app)
    register_error_handlers(app)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    return app
