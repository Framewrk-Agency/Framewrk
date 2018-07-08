from flask import Flask, url_for, render_template, Markup, redirect, request, Response
from wtforms import Form, BooleanField, StringField, PasswordField, validators
#from flask_assets import Environment, Bundle
import os
#from flask_static_compress import FlaskStaticCompress
from flask_migrate import Migrate
from flask_login import LoginManager
from mongoengine import connect
from flask_login import LoginManager, UserMixin
from flask_static_compress import FlaskStaticCompress
import sys
import logging
logging.basicConfig(level=logging.DEBUG)


from flask_wtf.csrf import CSRFProtect
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
#from app import app, db
from forms import LoginForm, RegistrationForm
from models import User
import app



app = Flask(__name__)
compress = FlaskStaticCompress(app)
app.static_folder = 'static'
db = connect(
    db='framewrk',
    username='todd',
    password='a9tw3rjw',
    host='mongodb://hackerdata-shard-00-01-gktww.gcp.mongodb.net:27017'
)
login = LoginManager(app)

app.config.from_object('config')
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_OUTPUT_DIR'] = '/build'
app.config['COMPRESSOR_STATIC_PREFIX'] = '/static'
'''connect(
    db='framewrk',
    username='todd',
    password='a9tw3rjw',
    host='mongodb://hackerdata-shard-00-01-gktww.gcp.mongodb.net:27017'
)'''
login.login_view = 'login'



@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('/login.html', form=form, template="home-page")


@app.route("/dashboard", methods=['POST'])
def dashboard():
    '''var user_id = req.body.id;
    var token = req.body.token;
    var geo = req.body.geo;
     res.render('created', {layout: 'default', template: 'created-page'});'''
    return render_template('/dashboard.html', template="dashboard-template")


'''@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)'''

import models, forms
