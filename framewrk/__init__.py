import os
import sys
from flask import Flask
from config import BaseConfig
# from models import User, users, login_manager


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.BaseConfig')


    from . import db
    from . import views
    db.init_app(app)
    app.register_blueprint(views.main)

    return app
