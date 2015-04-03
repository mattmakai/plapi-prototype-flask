from flask import Flask, request
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
api = Api(app)


from .resources import ProgrammingLanguage, ProgrammingLanguageList
api.add_resource(ProgrammingLanguage, '/programming-language/<string:slug>/',
                 endpoint='pl_ep')
api.add_resource(ProgrammingLanguageList, '/programming-languages/')

