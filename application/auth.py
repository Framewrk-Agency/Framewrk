from flask import url_for, render_template, redirect, request, flash, Response, Blueprint
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash
from .forms import LoginForm, SignupForm
from .models import db, User
from .assets import compile_assets
from .import login_manager


auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
compile_assets(app)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    """User login page."""
    # Bypass Login screen if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard'))
    login_form = LoginForm(request.form)
    # POST: Create user and redirect them to the app
    if request.method == 'POST':
        if login_form.validate():
            # Get Form Fields
            email = request.form.get('email')
            password = request.form.get('password')
            # Validate Login Attempt
            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    next = request.args.get('next')
                    return redirect(next or url_for('main_bp.dashboard'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login_page'))
    # GET: Serve Log-in page
    return render_template('login.html',
                           form=LoginForm(),
                           title='Log in | Flask-Login Tutorial.',
                           template='login-page',
                           body="Log in with your User account.")


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(name=name,
                            email=email,
                            password=generate_password_hash(password, method='sha256'),
                            website=website)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('main_bp.dashboard'))
            flash('A user already exists with that email address.')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template('/signup.html',
                           title='Create an Account | Flask-Login Tutorial.',
                           form=SignupForm(),
                           template='signup-page',
                           body="Sign up for a user account.")

'''@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    login_form = LoginForm()
    if request.method == 'GET':
        return render_template('/login.html', form=login_form, template="form-page")
    else:
        if login_form.validate():
            users = mongo.db.users
            login_attempt = users.find_one({'email': request.form['email']})
            if login_attempt:
                print('user exists')
                if bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.genSalt()):
                    session['email'] = request.form['email']
                    return render_template('/dashboard.html', template="dashbord-template")
    return 'Invalid username/password combination'




@auth_bp.route('/', methods=['GET', 'POST'])
def signup():
    """Signup Form."""
    signup_form = SignupForm()
    if request.method == 'POST':
        if signup_form.validate():
            users = mongo.db.users
            bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.genSalt())
            existing_user = users.find_one({'email': request.form['email']})
            if existing_user is None:
                document = {'name': request.form['name'],
                            'email': request.form['email'],
                            'password': request.form['password'],
                            'website': request.form['website']
                            }
            # login_user(user)
            users.insert({'email': document['email']}, document, upsert=True)
            flash('Logged in successfully.')
            return render_template('/dashboard.html', template="dashbord-template")
    return render_template('/signup.html', form=signup_form, template="form-page")'''


# somewhere to logout
@auth_bp.route("/logout")
@login_required
def logout():
    """User explicity logs out."""
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@auth_bp.errorhandler(401)
def page_not_found(e):
    """User attempts to reach broken page."""
    return Response('<p>Login failed</p>')


@auth_bp.route("/logout")
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login_page'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login_page'))
