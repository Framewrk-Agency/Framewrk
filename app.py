from flask import Flask, url_for, render_template, Markup, redirect, request, flash, g, Session
from flask_assets import Environment, Bundle, build
from forms import LoginForm, SignupForm
import config
from models import User, users, login_manager
from db import users, questions, onboarding
import logging
import sys
import json
from sassutils.wsgi import SassMiddleware
import sass
from flask_fileupload import FlaskFileUpload
from flask_fileupload.storage.s3storage import S3Storage

# Logs
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates",)
app.config.from_object('config.ProductionConfig')

# s3
# s3storage = S3Storage()
# ffu = FlaskFileUpload(app, s3storage)

app.config.from_object('config.ProductionConfig')
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/scss', '/build/all.css', '/build/all.css')
})

scss = Bundle('scss/main.scss', 'scss/components/onboarding.scss', 'scss/components/_tooltip.scss', filters='pyscss', output='build/style.css',)
js = Bundle('js/charts.js', 'js/dragdrop.js', 'js/interact.js', 'js/recordWorker.js', 'js/sidebar.js', output='build/main.js')

assets = Environment(app)
assets.register('js_all', scss)
assets.register('scss_all', js)
js.build()
scss.build()

assets.init_app(app)
session = Session()


@app.before_request
def before_request():
    """Handle multiple users."""
    g.user = None
    if 'username' in session:
        g.user = session['username']


'''@app.url_value_preprocessor
def url_value_preprocessor(endpoint, values):
    """Validate before every request."""
    if 'username' in session:
        return session
    else:
        if request.args.get('email'):
            session.permanent = True
            email = request.args.get('email')
            username = email.split('@')[0]'''


@app.route('/', methods=['GET', 'POST'])
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate():
            return render_template('/dashboard.html', template="dashbord-template")
        else:
            flash('Invalid login')
    return render_template('/login.html', form=login_form, template="form-page")


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    """Landing Page Dashboard."""
    return render_template('/dashboard.html', data=onboarding, template="dashboard-template")


@app.route("/frame", methods=['GET', 'POST'])
def frame():
    app.template_folder = 'templates'
    return render_template('/frame.html',)


@app.route('/question', methods=['GET', 'POST'])
def question():
    """Entry point for quetions."""
    return render_template('/question.html', template='qotd-template')


@app.route('/discover', methods=['GET', 'POST'])
def discover():
    """Entry point for discover."""
    return render_template('/discover.html', template='questionaire-template')


@app.route('/interact', methods=['GET', 'POST'])
def interact():
    """Audio submission portal."""
    return render_template('/interact.html', template='interact-template')


@app.route('/onboarding-business', methods=['GET', 'POST'])
def onboardingbusiness():
    """User business-type onboarding."""
    data = json.loads(onboarding)
    return render_template('/onboarding.html', category=data.category, questiontext=data.question)


@app.route('/onboarding-customers', methods=['GET', 'POST'])
def onboardingcustomers():
    """User onboarding question."""
    return render_template('/onboarding.html', category='customers', questiontext='What stage are you at in customer understanding?')


@app.route('/onboarding-competition', methods=['GET', 'POST'])
def onboardingcompetition():
    """User competition onboarding."""
    return render_template('/onboarding.html', category='competition', questiontext='What stage are your competitors at?')


@app.route('/onboarding-team', methods=['GET', 'POST'])
def onboardingteam():
    """User team onboarding."""
    return render_template('/onboarding.html', category='team', questiontext='What stage is your team development at?')
