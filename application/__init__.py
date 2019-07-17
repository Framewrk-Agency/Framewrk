from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


db = SQLAlchemy()
login_manager = LoginManager()
sess = Session()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    sess.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from . import demo
        from .assets import compile_assets, demo_assets
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(demo.demo_bp)
        compile_assets(app)
        demo_assets(app)

        # Create Database Models
        db.create_all()

        return app
