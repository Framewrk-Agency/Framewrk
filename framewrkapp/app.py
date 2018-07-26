from flask import Flask, url_for, render_template, Markup, redirect, request
from flask_static_compress import FlaskStaticCompress
import logging
from forms import LoginForm, SignupForm
from models import User, users, login_manager
from flask_login import login_user
from db import users_col, questions_col, mindspaces_col
# Logs
logging.basicConfig(level=logging.DEBUG)

# Initiate app
app = Flask(__name__)
# login_manager.init_app(app)

# Static Files
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_OUTPUT_DIR'] = 'build'
app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
app.static_folder = 'static'
compress = FlaskStaticCompress(app)


@app.route('/', methods=['GET', 'POST'])
def signup():
    """Signup Form."""
    signup_form = SignupForm()
    return render_template('/signup.html', form=signup_form, template="form-page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    login_form = LoginForm(request.form)
    # login_form = model_form(User, base_class=LoginForm)
    if request.method == 'POST' and login_form.validate():
        email = login_form['email']
        # if request.form['password'] == users[email]['password']:
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
