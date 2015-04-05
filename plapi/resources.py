from flask import request
from flask.ext.restful import Resource, marshal_with, abort, reqparse

from .models import ParadigmModel, PLAPIResource, ProgrammingLanguageModel
from . import db

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help="Resource name.")
parser.add_argument('uri', type=str, help="Full path URI for this resource.")

class PLAPIResourcesList(Resource):
    @marshal_with(PLAPIResource.marshal_fields)
    def get(self):
        prs = PLAPIResource.query.all()
        for r in prs:
            r.uri = request.base_url + r.uri
        return prs

    def post(self):
        args = parser.parse_args()
        prs = PLAPIResource()
        prs.name = args['name']
        prs.uri = args['uri']
        db.session.add(prs)
        db.session.commit()
        return {}, 201


class ProgrammingLanguage(Resource):
    @marshal_with(ProgrammingLanguageModel.marshal_fields)
    def get(self, slug):
        languages = ProgrammingLanguageModel.query.filter_by(slug=slug)
        if languages.count() > 0:
            return languages.first()
        return abort(404)


class ProgrammingLanguagesList(Resource):
    @marshal_with(ProgrammingLanguageModel.marshal_fields)
    def get(self, **kwargs):
        return ProgrammingLanguageModel.query.all()

