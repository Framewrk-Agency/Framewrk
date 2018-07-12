import flask_login
from flask_login import login_manager


users = {'foo@bar.tld': {'password': 'secret'}}

# User Sessions
login_manager = flask_login.LoginManager()
login_manager.login_view = 'login'


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'
