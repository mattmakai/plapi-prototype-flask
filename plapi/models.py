from flask.ext.restful import fields

from . import db


class User(db.Model):
    """
        An account with access to the PLAPI service.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)


class Framework(db.Model):
    """
        A code library for a specific language that makes implementing
        some goal easier. For example, Django makes creating Python
        web applications easier.
    """
    __tablename__ = 'frameworks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256), unique=True)
    homepage_url = db.Column(db.String(2048))
    code_repository_url = db.Column(db.String(2048))


class ParadigmModel(db.Model):
    """
        A programming paradigm. For example, imperative or functional.
    """
    __tablename__ = 'paradigms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256), unique=True)

    marshal_fields = {
        'name': fields.String,
        'uri': fields.Url('paradigm_ep', absolute=True),
    }


class PLAPIResource(db.Model):
    """
        Stores information about all the available endpoints in PLAPI.
    """
    __tablename__ = 'plapi_resources'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    uri = db.Column(db.String(2048))

    marshal_fields = {
        'name': fields.String,
        'uri': fields.String,
    }


    def generate_curl(self):
        curl = 'curl --data "'
        curl += 'name' + '=' + self.name
        curl += '&' + 'uri' + '=' + self.uri
        return curl + '" http://localhost:5001/'


class ProgrammingLanguageModel(db.Model):
    """
        A programming language, such as Python or C, and related
        information.
    """
    __tablename__ = 'programming_languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256), unique=True)
    homepage_url = db.Column(db.String(2048))

    marshal_fields = {
        'name': fields.String,
        'uri': fields.Url('pl_ep', absolute=True),
        'homepage_url': fields.String,
    }

