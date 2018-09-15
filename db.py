import pymongo
from pymongo import MongoClient, database
import os
import sys
from bson.json_util import dumps
import json

# DB Creds
# mongo = MongoClient('mongodb+srv://todd:a9tw3rjw@hackerdata-gktww.gcp.mongodb.net/admin?retryWrites=true', maxPoolSize=50, connect=False)
# db = database.Database(mongo, 'framewrk')

# stitch


client = pymongo.MongoClient('mongodb://toddbirchard%40gmail.com:a9tw3rjw@stitch.mongodb.com:27020/?authMechanism=PLAIN&authSource=%24external&ssl=true&appName=framewrk-iroeq:mongodb-atlas:local-userpass')

db = client["framewrk"]

users_col = db['users']
questions_col = db['questions']
onboarding_col = db['onboarding']

users = json.loads(dumps(db.users.find()))
questions = json.loads(dumps(db.questions.find()))
onboarding = json.loads(dumps(db.onboarding.find()))

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print('questions = ', questions)
