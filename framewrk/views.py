
# from flask_fileupload import FlaskFileUpload
# from flask_fileupload.storage.s3storage import S3Storage
from flask import current_app, g
from flask.cli import with_appcontext
from flask import Flask, url_for, render_template, Markup, redirect, request, flash, g, Session
from jinja2 import TemplateNotFound
from .forms import LoginForm, SignupForm
import logging
import sys
import os
import json
from .db import get_db
from flask import Blueprint


main = Blueprint('main', __name__)


'''@main.before_request
def before_request():
    """Handle multiple users."""
    g.user = None
    if 'username' in session:
        g.user = session['username']'''


'''@main.url_value_preprocessor
def url_value_preprocessor(endpoint, values):
    """Validate before every request."""
    if 'username' in session:
        return session
    else:
        if request.args.get('email'):
            session.permanent = True
            email = request.args.get('email')
            username = email.split('@main.')[0]'''




@main.route('/', methods=['GET', 'POST'])
def signup():
    """Signup Form."""
    signup_form = SignupForm()
    if request.method == 'POST':
        if signup_form.validate():
            document = {'name': request.form['name'],
                        'email': request.form['email'],
                        'password': request.form['password'],
                        'website': request.form['website']
                        }
            # login_user(user)
            result = users.replace_one({'email': document['email']}, document, upsert=True)
            print('result = ', result)
            sys.stdout.flush()
            flash('Logged in successfully.')
            return render_template('/dashboard.html', template="dashbord-template")
    return render_template('/signup.html', form=signup_form, template="form-page")


@main.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate():
            return render_template('/dashboard.html', template="dashbord-template")
        else:
            flash('Invalid login')
    return render_template('/login.html', form=login_form, template="form-page")


@main.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    """Landing Page Dashboard."""
    return render_template('/dashboard.html', data=onboarding, template="dashboard-template")


@main.route("/frame", methods=['GET', 'POST'])
def frame():
    app.template_folder = 'templates'
    return render_template('/frame.html',)


@main.route('/question', methods=['GET', 'POST'])
def question():
    """Entry point for quetions."""
    return render_template('/question.html', template='qotd-template')


@main.route('/discover', methods=['GET', 'POST'])
def discover():
    """Entry point for discover."""
    return render_template('/discover.html', template='questionaire-template')


@main.route('/interact', methods=['GET', 'POST'])
def interact():
    """Audio submission portal."""
    return render_template('/interact.html', template='interact-template')


@main.route('/onboarding-business', methods=['GET', 'POST'])
def onboardingbusiness():
    """User business-type onboarding."""
    data = json.loads(onboarding)
    return render_template('/onboarding.html', category=data.category, questiontext=data.question)


@main.route('/onboarding-customers', methods=['GET', 'POST'])
def onboardingcustomers():
    """User onboarding question."""
    return render_template('/onboarding.html', category='customers', questiontext='What stage are you at in customer understanding?')


@main.route('/onboarding-competition', methods=['GET', 'POST'])
def onboardingcompetition():
    """User competition onboarding."""
    return render_template('/onboarding.html', category='competition', questiontext='What stage are your competitors at?')


@main.route('/onboarding-team', methods=['GET', 'POST'])
def onboardingteam():
    """User team onboarding."""
    return render_template('/onboarding.html', category='team', questiontext='What stage is your team development at?')
