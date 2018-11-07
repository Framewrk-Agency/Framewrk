from flask import current_app, g
from flask import Flask, url_for, render_template, Markup, redirect, request, flash, g, Session
from jinja2 import TemplateNotFound
from forms import LoginForm, SignupForm
import os
import json
from flask import Blueprint

main = Blueprint('main', __name__)

'''@main.url_value_preprocessor
def url_value_preprocessor(endpoint, values):
    """Validate before every request."""
    if 'username' in session:
        return session
    else:
        if request.args.get('email'):
            session.permanent = True
            email = request.args.get('email')
            username = email.split('@main.')[0]'''


@main.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    """Landing Page Dashboard."""
    return render_template('/dashboard.html', data=g.db['onboarding'], template="dashboard-template")


@main.route("/frame", methods=['GET', 'POST'])
@login_required
def frame():
    main.template_folder = 'templates'
    return render_template('/frame.html',)


@main.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    """Entry point for quetions."""
    return render_template('/question.html', template='qotd-template')


@main.route('/discover', methods=['GET', 'POST'])
@login_required
def discover():
    """Entry point for discover."""
    return render_template('/discover.html', template='questionaire-template')


@main.route('/interact', methods=['GET', 'POST'])
@login_required
def interact():
    """Audio submission portal."""
    return render_template('/interact.html', template='interact-template')


@main.route('/onboarding-business', methods=['GET', 'POST'])
@login_required
def onboardingbusiness():
    """User business-type onboarding."""
    data = json.loads(onboarding)
    return render_template('/onboarding.html', category=data.category, questiontext=data.question)


@main.route('/onboarding-customers', methods=['GET', 'POST'])
@login_required
def onboardingcustomers():
    """User onboarding question."""
    return render_template('/onboarding.html', category='customers', questiontext='What stage are you at in customer understanding?')


@main.route('/onboarding-competition', methods=['GET', 'POST'])
def onboardingcompetition():
    """User competition onboarding."""
    return render_template('/onboarding.html', category='competition', questiontext='What stage are your competitors at?')


@main.route('/onboarding-team', methods=['GET', 'POST'])
def onboardingteam():
    """User team onboarding."""
    return render_template('/onboarding.html', category='team', questiontext='What stage is your team development at?')


@main.route('/directory', methods=['GET'])
def directory():
    """List all templates."""
    template_urls = os.listdir('templates')
    return render_template('/directory.html', templates=template_urls, template='directory-template')
