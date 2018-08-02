from flask import Flask, url_for, render_template, Markup, redirect, request
from flask_static_compress import FlaskStaticCompress
from forms import LoginForm, SignupForm
from models import User, users, login_manager
from db import users_col, questions_col, mindspaces_col
import logging

# Logs
logging.basicConfig(level=logging.DEBUG)

# Initiate apps
app = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates")
compress = FlaskStaticCompress(app)
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
app.config['COMPRESSOR_OUTPUT_DIR'] = 'sdist'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'
app.static_folder = 'static'


@app.route('/', methods=['GET', 'POST'])
def signup():
    """Signup Form."""
    signup_form = SignupForm()
    return render_template('/signup.html', form=signup_form, template="form-page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        email = login_form['email']
        user = User()
        user.id = email
        login_user(user)
        request.flash('Logged in successfully.')
        next = app.request.args.get('next')
        if not is_safe_url(next):
            return app.abort(400)
        return app.redirect(next or app.url_for('index'))
    return render_template('/login.html', form=login_form, template="form-page")


@app.route("/dashboard", methods=['POST'])
def dashboard():
    """Default Dashboard."""
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
