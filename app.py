from flask import Flask, url_for, render_template, Markup, redirect, request
from flask_static_compress import FlaskStaticCompress
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
app.config['COMPRESSOR_CLASSES'] = [
    'text/css': LessCompressor,
    'text/less': LessCompressor,
    'text/javascript': JavaScriptCompressor,
]
app.static_folder = 'static'


@app.route('/', methods=['GET', 'POST'])
def signup():
    """Signup Form."""
    signup_form = SignupForm()
    return render_template('/signup.html', form=signup_form, error='', template="form-page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    login_form = LoginForm()
    return render_template('/login.html', form=login_form, template="form-page")


@app.route('/validate', methods=['POST'])
def validate():
    if "@" not in request.form['email']:
         error = Markup('<p class="error">Please submit a real email.</p>')
         return render_template('/index.html', error='Incorrect email.', template="home-template")
    elif request.form.validate():
        document = {'name': request.form['name'],
                'email': request.form.email,
                'password': request.form.password,
                'website': request.form.repo_url
                }
        # login_user(user)
        result = users_col.replace_one({'email': document['email']}, document, upsert=True)
        print('result = ', result)
        sys.stdout.flush()
        request.flash('Logged in successfully.')
        redirect('dashboard.html')


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
        return redirect(url_for('dashboard'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)'''