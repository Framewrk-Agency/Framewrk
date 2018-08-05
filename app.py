from flask import Flask, url_for, render_template, Markup, redirect, request, flash
from flask_static_compress import FlaskStaticCompress
from flask import session as login_session
from forms import LoginForm, SignupForm
from models import User, users, login_manager
from db import users_col, questions_col, mindspaces_col
import logging
import sys

# Logs
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates")
compress = FlaskStaticCompress(app)
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
app.config['COMPRESSOR_OUTPUT_DIR'] = 'sdist'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'
app.static_folder = 'static'
app.secret_key = '\xc3\xc1\xf2\xe9\xd8\x14\\\x16\x9a\xbf\xee\x07'


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
            result = users_col.replace_one({'email': document['email']}, document, upsert=True)
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
    return render_template('/dashboard.html', template="dashboard-template")


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
    """Entry point for interact."""
    return render_template('/interact.html', template='interact-template')


@app.route('/help', methods=['GET', 'POST'])
def help():
    """Entry point for help."""
    return render_template('/help.html', template='help-template')
