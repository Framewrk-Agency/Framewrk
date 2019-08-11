"""Database models."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String,
                     nullable=False,
                     unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    website = db.Column(db.String(60),
                        index=False,
                        unique=False,
                        nullable=True)
    created_on = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    last_login = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Question(db.Model):
    """Model for questions."""
    __tablename__ = 'questions'

    id = db.Column(db.Integer,
                   primary_key=True)
    num = db.Column(db.Integer)
    question = db.Column(db.Text,
                         nullable=False,
                         unique=False)
    question_type = db.Column(db.Text,
                              nullable=False,
                              unique=False)
    info = db.Column(db.Text,
                     nullable=False,
                     unique=False)
    variable = db.Column(db.Text,
                         nullable=False,
                         unique=False)
    value = db.Column(db.Text,
                      nullable=False,
                      unique=False)


class FeedItem(db.Model):
    """Model for feed items."""
    __tablename__ = 'feed'

    id = db.Column(db.Integer,
                   primary_key=True)
    type = db.Column(db.String,
                     nullable=False,
                     unique=False)
    title = db.Column(db.Text,
                      nullable=False,
                      unique=False)
    image = db.Column(db.Text,
                      nullable=False,
                      unique=False)
