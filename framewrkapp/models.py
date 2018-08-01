import flask_login
from flask import request
import flask_login

users = {'test@example.com': {'password': 'secret'}}
login_manager = flask_login.LoginManager()


class User(flask_login.UserMixin):
    """Generic user class."""

    pass


@login_manager.user_loader
def user_loader(email):
    """Find users by email."""
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    """Not sure what this does yet."""
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated= request.form['password'] == users[email]['password']
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    """User Failed Login."""
    return 'Unauthorized'
