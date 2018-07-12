from flask import Flask, url_for, render_template, Markup, redirect, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_static_compress import FlaskStaticCompress
import logging
from flask_wtf.csrf import CSRFProtect
from werkzeug.urls import url_parse
from forms import LoginForm, SignupForm
import app
from models import user
from flask_login import login_manager, login_user, is_safe_url

# Logs
logging.basicConfig(level=logging.DEBUG)

# Initiate app
app = Flask(__name__)
login_manager.init_app(app)

# Static Files
compress = FlaskStaticCompress(app)
app.static_folder = 'static'
app.config.from_object('config')
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_OUTPUT_DIR'] = '/build'
app.config['COMPRESSOR_STATIC_PREFIX'] = '/static'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('/home.html', template="home-template")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if app.request.method == 'GET':
        return render_template('/login.html', form=LoginForm, template="form-page")
    if LoginForm.validate_on_submit():
        login_user(user)
        app.flash('Logged in successfully.')
        next = app.request.args.get('next')
    if not is_safe_url(next):
        return app.abort(400)
    return app.redirect(next or app.url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    return render_template('/signup.html', form=form, template="form-page")


@app.route("/dashboard", methods=['POST'])
def dashboard():
    '''var user_id = req.body.id;
    var token = req.body.token;
    var geo = req.body.geo;
     res.render('created', {layout: 'default', template: 'created-page'});'''
    return render_template('/dashboard.html', template="dashboard-template")


'''@app.route('/validateSignup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)'''
