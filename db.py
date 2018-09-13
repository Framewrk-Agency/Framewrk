from pymongo import MongoClient, database
import os
import sys
from bson.json_util import dumps
import json

# DB Creds
mongo = MongoClient('mongodb+srv://todd:a9tw3rjwhackerdata-gktww.gcp.mongodb.net/admin', maxPoolSize=50, connect=False)
db = database.Database(mongo, 'framewrk')

users_col = db['users']
questions_col = db['questions']
mindspaces_col = db['mindspaces']
onboarding_col = db['onboarding']

users = json.loads(dumps(db.users.find()))
questions = json.loads(dumps(db.questions.find()))
mindspaces = json.loads(dumps(db.mindspaces.find()))
onboarding = json.loads(dumps(db.onboarding.find()))

print('onboarding = ', onboarding)
sys.stdout.flush()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
