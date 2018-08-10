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
            return redirect('/dashboard.html', template="dashbord-template")
        else:
            flash('Whoops! Looks liked we missed a few things.')
            return render_template('/signup.html', form=signup_form, template="form-page")
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

    @app.route('/question', methods=['GET', 'POST'])
    def question():
        """Entry point for quetions."""
        return render_template('/question.html', template='qotd-template')


    @app.route('/interact', methods=['GET', 'POST'])
    def onboardingtype():
        """Business-type onboarding."""
        return render_template('/onboarding.html', category='business', questiontext='What type of business do you have?')


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    """Landing Page Dashboard."""
    return render_template('/dashboard.html', template="dashboard-template")


@app.route("/frame", methods=['GET', 'POST'])
def frame():
    app.template_folder = 'templates'
    return render_template('/frame.html',)
