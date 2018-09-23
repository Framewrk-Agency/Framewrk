from flask import Flask, url_for, render_template, Markup, redirect, request, flash, g, Session
from flask_assets import Environment, Bundle, build
from forms import LoginForm, SignupForm
import config
from models import User, users, login_manager
from db import users, questions, onboarding
import logging
import sys
import os
import json
from sassutils.wsgi import SassMiddleware
import sass
# from flask_fileupload import FlaskFileUpload
# from flask_fileupload.storage.s3storage import S3Storage

# Logs

logging.basicConfig(level=logging.DEBUG)

framewrk = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates",)
framewrk.config.from_object('config.ProductionConfig')

framewrk.wsgi_framewrk = SassMiddleware(framewrk.app, {
    'app': ('static/scss', '/build/all.css', '/build/all.css')
})

scss = Bundle('scss/main.scss', 'scss/components/onboarding.scss', 'scss/components/_tooltip.scss', filters='pyscss', output='build/style.css',)
js = Bundle('js/charts.js', 'js/dragdrop.js', 'js/interact.js', 'js/recordWorker.js', 'js/sidebar.js', output='build/main.js')

assets = Environment(framewrk)
assets.register('js_all', scss)
assets.register('scss_all', js)
js.build()
scss.build()

assets.init_framewrk(framewrk)
session = Session()


@framewrk.before_request
def before_request():
    """Handle multiple users."""
    g.user = None
    if 'username' in session:
        g.user = session['username']


'''@framewrk.url_value_preprocessor
def url_value_preprocessor(endpoint, values):
    """Validate before every request."""
    if 'username' in session:
        return session
    else:
        if request.args.get('email'):
            session.permanent = True
            email = request.args.get('email')
            username = email.split('@')[0]'''


@framewrk.route('/', methods=['GET', 'POST'])
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


@framewrk.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate():
            return render_template('/dashboard.html', template="dashbord-template")
        else:
            flash('Invalid login')
    return render_template('/login.html', form=login_form, template="form-page")


@framewrk.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    """Landing Page Dashboard."""
    return render_template('/dashboard.html', data=onboarding, template="dashboard-template")


@framewrk.route("/frame", methods=['GET', 'POST'])
def frame():
    framewrk.template_folder = 'templates'
    return render_template('/frame.html',)


@framewrk.route('/question', methods=['GET', 'POST'])
def question():
    """Entry point for quetions."""
    return render_template('/question.html', template='qotd-template')


@framewrk.route('/discover', methods=['GET', 'POST'])
def discover():
    """Entry point for discover."""
    return render_template('/discover.html', template='questionaire-template')


@framewrk.route('/interact', methods=['GET', 'POST'])
def interact():
    """Audio submission portal."""
    return render_template('/interact.html', template='interact-template')


@framewrk.route('/onboarding-business', methods=['GET', 'POST'])
def onboardingbusiness():
    """User business-type onboarding."""
    data = json.loads(onboarding)
    return render_template('/onboarding.html', category=data.category, questiontext=data.question)


@framewrk.route('/onboarding-customers', methods=['GET', 'POST'])
def onboardingcustomers():
    """User onboarding question."""
    return render_template('/onboarding.html', category='customers', questiontext='What stage are you at in customer understanding?')


@framewrk.route('/onboarding-competition', methods=['GET', 'POST'])
def onboardingcompetition():
    """User competition onboarding."""
    return render_template('/onboarding.html', category='competition', questiontext='What stage are your competitors at?')


@framewrk.route('/onboarding-team', methods=['GET', 'POST'])
def onboardingteam():
    """User team onboarding."""
    return render_template('/onboarding.html', category='team', questiontext='What stage is your team development at?')
