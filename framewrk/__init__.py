import os
import sys
from flask import Flask, g
import config
import flask_login
#from flask_pymongo import PyMongo
# from models import User, users, login_manager


def create_app():
    """Construct app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.BaseConfig')
    login = flask_login.LoginManager()

    with app.app_context():
        from . import views
        from . import auth
        login.init_app(app)
        #mongo = PyMongo(app, app.config['MONGO_URI'])
        # g.db = mongo
        app.register_blueprint(auth.auth)
        app.register_blueprint(views.main)

        return app
