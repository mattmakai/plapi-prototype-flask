from flask.ext.restful import Resource, fields, marshal_with

from .models import ProgrammingLanguageModel

programming_language_fields = {
    'name': fields.String,
    'uri': fields.Url('pl_ep'),
}

class ProgrammingLanguage(Resource):
    @marshal_with(programming_language_fields)
    def get(self, slug):
        languages = ProgrammingLanguageModel.query.filter_by(slug=slug)
        if languages.count() > 0:
            return languages.first()
        return {'error': 'No language found.'}, 404


class ProgrammingLanguageList(Resource):
    @marshal_with(programming_language_fields)
    def get(self, **kwargs):
        return ProgrammingLanguageModel.query.all()
