from wtforms import Form, StringField, PasswordField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from models import User


class SignupForm(Form):
    """User Signup."""

    name = StringField('Name', validators=[
        DataRequired()
        ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
        ])
    password = PasswordField('Password', validators=[
        DataRequired()
        ])
    password2 = PasswordField('Repeat Password', validators=[
        DataRequired(),
        EqualTo('password')
        ])
    website = StringField('Website', validators=[
        DataRequired()
        ])
    submit = SubmitField('Register')

    def validate_email(self, email):
        """Email validation."""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LoginForm(Form):
    """User Login."""

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    website = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')
