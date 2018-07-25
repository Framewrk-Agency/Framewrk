import pymongo
import os
import requests
import sys

# DB Creds
mongo = pymongo.MongoClient('mongodb+srv://todd:a9tw3rjw@hackerdata-gktww.gcp.mongodb.net/admin', maxPoolSize=50, connect=False)
db = pymongo.database.Database(mongo, 'framewrk',)
users_col = pymongo.collection.Collection(db, 'users')
questions_col = pymongo.collection.Collection(db, 'questions')
mindspaces_col = pymongo.collection.Collection(db, 'users')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
