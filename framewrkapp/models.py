from flask_login import UserMixin
from mongoengine import *

class User(Document):
    email = StringField(required=True)
    password = StringField(max_length=50, required=True)
    website = StringField(max_length=50, required=True)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
