"""Main routes."""
from flask.cli import with_appcontext
from flask import url_for, render_template, request
import json
from flask import current_app as app
from flask import Blueprint
from flask_login import login_required


main_bp = Blueprint('main', __name__)


@main_bp.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    """Landing Page Dashboard."""
    return render_template('/dashboard.html', data=g.db['onboarding'], template="dashboard-template")


@main_bp.route("/frame", methods=['GET', 'POST'])
@login_required
def frame():
    app.template_folder = 'templates'
    return render_template('/frame.html',)


@main_bp.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    """Entry point for quetions."""
    return render_template('/question.html', template='qotd-template')


@main_bp.route('/discover', methods=['GET', 'POST'])
@login_required
def discover():
    """Entry point for discover."""
    return render_template('/discover.html', template='questionaire-template')


@main_bp.route('/interact', methods=['GET', 'POST'])
@login_required
def interact():
    """Audio submission portal."""
    return render_template('/interact.html', template='interact-template')


@main_bp.route('/onboarding-business', methods=['GET', 'POST'])
@login_required
def onboardingbusiness():
    """User business-type onboarding."""
    data = json.loads(onboarding)
    return render_template('/onboarding.html', category=data.category, questiontext=data.question)


@main_bp.route('/onboarding-customers', methods=['GET', 'POST'])
@login_required
def onboardingcustomers():
    """User onboarding question."""
    return render_template('/onboarding.html', category='customers', questiontext='What stage are you at in customer understanding?')


@main_bp.route('/onboarding-competition', methods=['GET', 'POST'])
def onboardingcompetition():
    """User competition onboarding."""
    return render_template('/onboarding.html', category='competition', questiontext='What stage are your competitors at?')


@main_bp.route('/onboarding-team', methods=['GET', 'POST'])
def onboardingteam():
    """User team onboarding."""
    return render_template('/onboarding.html', category='team', questiontext='What stage is your team development at?')
