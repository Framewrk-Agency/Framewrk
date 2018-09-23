from flask import current_app, g
from flask.cli import with_appcontext
import click

import pymongo
from pymongo import MongoClient, database
from bson.json_util import dumps
import json


# stitch

def get_db():
    if 'db' not in g:
        client = MongoClient(current_app.config['URI'])
        g.db = client["framewrk"]
        g.users_col = db['users']
        g.questions_col = db['questions']
        g.onboarding_col = db['onboarding']

        users = json.loads(dumps(db.users.find()))
        questions = json.loads(dumps(db.questions.find()))
        onboarding = json.loads(dumps(db.onboarding.find()))

        print('questions = ', questions)
        return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
