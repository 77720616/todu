__author__ = 'nan'
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect

app = Flask(__name__)
app.config.from_object('config')

# db = MongoEngine(app)
db = connect('todo')

from app import views,models
