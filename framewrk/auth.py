import sys
import os
from flask import Flask, url_for, render_template, Markup, redirect, request, flash, g, session, Response, Blueprint
from flask import current_app as app
import logging
import json
import sass
import bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, login_manager
from flask_assets import Environment, Bundle, build
from .forms import LoginForm, SignupForm
from .user import User


auth = Blueprint('auth', __name__)
assets = Environment(app)
scss = Bundle('scss/main.scss', 'scss/components/forms.scss', filters='libsass', output='build/css/style.css')
assets.register('scss_all', scss)
# scss.build(disable_cache=None)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    login_form = LoginForm(request.form)
    if request.method == 'GET':
        return render_template('/login.html', form=login_form, template="form-page")
    else:
        if login_form.validate():
            users = 'placeholder'
            existing_user = users.find_one({'email': request.form['email']})
            print('attempted login = ', existing_user)
            sys.stdout.flush()
            if existing_user:
                print('user exists')
                sys.stdout.flush()
                if bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.genSalt()):
                    session['email'] = request.form['email']
                    return render_template('/dashboard.html', template="dashbord-template")
    return 'Invalid username/password combination'




@auth.route('/', methods=['GET', 'POST'])
def signup():
    """Signup Form."""
    signup_form = SignupForm(request.form)
    if request.method == 'POST':
        if signup_form.validate():
            users = mongo.db.users
            existing_user = users.find_one({'email': request.form['email']})
            print('attempted signup = ', existing_user)
            sys.stdout.flush()

            if existing_user is None:
                user_document = {'name': request.form['name'],
                            'email': request.form['email'],
                            'password': bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.genSalt()),
                            'website': request.form['website']
                            }
                users.insertOne({user_document})
                flash('Signed up successfully.')
                redirect(url_for('dashboard'))

            else:
                return 'That username already exists'
    return render_template('/signup.html', form=signup_form, template="form-page")


'''@login_manager.user_loader
def load_user(email):
    users = mongo.db.users
    return users.find_one({'email': email})
'''
# somewhere to logout
@auth.route("/logout")
@login_required
def logout():
    """User explicity logs out."""
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@auth.errorhandler(401)
def page_not_found(e):
    """User attempts to reach broken page."""
    return Response('<p>Login failed</p>')
