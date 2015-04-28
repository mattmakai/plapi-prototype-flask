from flask import Flask, request
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
api = Api(app)


from .resources import PLAPIResourcesList, Paradigm, ParadigmList
from .resources import ProgrammingLanguage, ProgrammingLanguagesList

api.add_resource(PLAPIResourcesList, '/', endpoint='plapi_ep')
api.add_resource(ProgrammingLanguage, '/programming-language/<string:slug>/',
                 endpoint='pl_ep')
api.add_resource(ProgrammingLanguagesList, '/programming-languages/')
api.add_resource(Paradigm, '/paradigm/<string:slug>/', endpoint='paradigm_ep')
api.add_resource(ParadigmList, '/paradigms/')
