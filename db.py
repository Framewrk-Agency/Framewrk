import pymongo
from pymongo import MongoClient, database
from bson.json_util import dumps
import json
from config import URI


# stitch


client = MongoClient(URI)

db = client["framewrk"]

users_col = db['users']
questions_col = db['questions']
onboarding_col = db['onboarding']

users = json.loads(dumps(db.users.find()))
questions = json.loads(dumps(db.questions.find()))
onboarding = json.loads(dumps(db.onboarding.find()))

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print('questions = ', questions)
