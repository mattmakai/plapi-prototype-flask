from flask import request
from flask.ext.restful import Resource, marshal_with

from .models import ParadigmModel, PLAPIResource, ProgrammingLanguageModel


class PLAPIResourcesList(Resource):
    @marshal_with(PLAPIResource.marshal_fields)
    def get(self):
        prs = PLAPIResource.query.all()
        for r in prs:
            r.uri = request.base_url + r.uri
        return prs


class ProgrammingLanguage(Resource):
    @marshal_with(ProgrammingLanguageModel.marshal_fields)
    def get(self, slug):
        languages = ProgrammingLanguageModel.query.filter_by(slug=slug)
        if languages.count() > 0:
            return languages.first()
        return {'error': 'No language found.'}, 404


class ProgrammingLanguagesList(Resource):
    @marshal_with(ProgrammingLanguageModel.marshal_fields)
    def get(self, **kwargs):
        return ProgrammingLanguageModel.query.all()

