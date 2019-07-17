"""Demo routes."""
from flask import url_for, render_template
from flask import current_app as app
from flask import Blueprint, request
from .models import Question

demo_bp = Blueprint('demo_bp', __name__)


@demo_bp.route("/", methods=['GET'])
def demo():
    """Demo Homepage."""
    return render_template('/demo/demo.html',
                           template="demo-template")


@demo_bp.route("/login-demo/", methods=['GET'])
def login():
    """Login page."""
    return render_template('/demo/login.html',
                           template="login-template")


@demo_bp.route("/signup-demo/", methods=['GET'])
def signup():
    """Signup page."""
    return render_template('/demo/signup.html',
                           template="signup-template")


@demo_bp.route("/signup-complete/", methods=['GET'])
def signup_complete():
    """Signup complete page."""
    return render_template('/demo/signupcomplete.html',
                           template="signup-template")


@demo_bp.route("/question/<int:num>/", methods=['GET'])
def question(num):
    """Question and answer page."""
    if request.method == 'GET':
        questionGroup = Question.query.filter(Question.num == num).from_self().all()
        answers = [answer.value for answer in questionGroup if '_text' in answer.variable]
        responses = [response.value for response in questionGroup if '_response' in response.variable]
        tooltips = [response.value for response in questionGroup if '_hover' in response.variable]
        questionType = questionGroup[0].question_type
        if questionType == 'Multiple Choice':
            return render_template('/demo/question-multiplechoice.html',
                                   question=questionGroup[0].question,
                                   choices=answers,
                                   responses=responses,
                                   tooltips=tooltips,
                                   # variables=variables,
                                   explanation=questionGroup[0].info,
                                   template="question-multiplechoice")
        return render_template('/demo/question-freeform.html',
                               question=questionGroup[0].question,
                               choices=answers,
                               responses=responses,
                               tooltips=tooltips,
                               # variables=variables,
                               explanation=questionGroup[0].info,
                               template="question-freeform")
