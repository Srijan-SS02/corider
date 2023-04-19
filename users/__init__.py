from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://localhost:27017/')
db = client['usersdatabase']

users_collection = db['users']

from users import api