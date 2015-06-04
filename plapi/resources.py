from flask import request
from flask.ext.restful import Resource, marshal_with, abort, reqparse

from .models import (LibraryModel, ParadigmModel, PLAPIResource,
                     ProgrammingLanguageModel, )
from . import db


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
        languages = db.session.query(
            ProgrammingLanguageModel).filter_by(slug=slug, is_visible=True)
        if languages.count() > 0:
            return languages.first()
        return abort(404)

    def post(self, slug):
        if db.session.query(ProgrammingLanguageModel).filter_by(
           slug=slug).count() > 0:
            return {'conflict': 'A programming language with this slug has '
                                'already been submitted to PLAPI.'}, 409
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str,
                            help="Programming language name.")
        parser.add_argument('homepage_url', type=str,
                            help="Homepage URL for the programming language.")
        args = parser.parse_args()
        pl = ProgrammingLanguageModel()
        pl.name = args['name']
        pl.homepage_url = args['homepage_url']
        pl.slug = slug
        db.session.add(pl)
        db.session.commit()
        return {}, 201


class ProgrammingLanguagesList(Resource):
    @marshal_with(ProgrammingLanguageModel.marshal_fields)
    def get(self, **kwargs):
        return db.session.query(
            ProgrammingLanguageModel).filter_by(is_visible=True).all()


class Paradigm(Resource):
    @marshal_with(ParadigmModel.marshal_fields)
    def get(self, slug):
        paradigms = ParadigmModel.query.filter_by(slug=slug)
        if paradigms.count() > 0:
            return paradigms.first()
        return abort(404)

    def post(self, slug):
        if db.session.query(ParadigmModel).filter_by(slug=slug).count() > 0:
            return {'conflict': 'A paradigm with this slug has already '
                                'been submitted to PLAPI.'}, 409
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str,
                            help="Programming paradigm name.")
        args = parser.parse_args()
        paradigm = ParadigmModel()
        paradigm.name = args['name']
        paradigm.slug = slug
        db.session.add(paradigm)
        db.session.commit()
        return {}, 201


class ParadigmList(Resource):
    @marshal_with(ParadigmModel.marshal_fields)
    def get(self, **kwargs):
        return db.session.query(
            ParadigmModel).filter_by(is_visible=True).all()


class Library(Resource):
    @marshal_with(LibraryModel.marshal_fields)
    def get(self, slug):
        libraries = db.session.query(LibraryModel).filter_by(slug=slug)
        if libraries.count > 0:
            return libraries.first()
        return abort(404)

    def post(self, slug):
        if db.session.query(LibraryModel).filter_by(slug=slug).count() > 0:
            return {'conflict': 'A library with this slug has already '
                                'been submitted to PLAPI.'}, 409
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str,
                            help="Library name.")
        parser.add_argument('homepage_url', type=str,
                            help="Homepage URL for the code library.")
        args = parser.parse_args()
        library = LibraryModel()
        library.name = args['name']
        library.slug = slug
        library.homepage_url = args['homepage_url']
        db.session.add(library)
        db.session.commit()
        return {}, 201


class LibrariesList(Resource):
    @marshal_with(LibraryModel.marshal_fields)
    def get(self, slug, **kwargs):
        programming_language_id = db.session.query(ProgrammingLanguageModel).\
            filter_by(slug=slug).first().id
        return db.session.query(LibraryModel).filter_by(is_visible=True,
            language=programming_language_id).all()

