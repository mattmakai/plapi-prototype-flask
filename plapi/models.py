from flask.ext.restful import fields
from itsdangerous import JSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(db.Model):
    """
        An account with access to the PLAPI service.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    password_hash = db.Column(db.String(256))

    def generate_api_token(self):
        serializer = Serializer(app.config['SECRET_KEY'])
        return serializer.dumps({'id': self.id})

    @staticmethod
    def verify_api_token(token):
        serializer = Serializer(app.config['SECRET_KEY'])
        try:
            data = serializer.loads(token)
        except BadSignature:
            # invalid token
            return None
        return User.query.get(data['id'])

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.email


class LibraryModel(db.Model):
    """
        A collection of code for a specific language that makes
        implementing some goal easier. For example, Django is a library
        that eases Python web application creation.
    """
    homepage_url = db.Column(db.String(2048))
    __tablename__ = 'libraries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256), unique=True)
    homepage_url = db.Column(db.String(2048))
    source_code_url = db.Column(db.String(2048))
    language = db.Column(db.Integer,
                         db.ForeignKey('programming_languages.id'))
    is_visible = db.Column(db.Boolean(), default=False,
                           server_default="false", nullable=False)
    code_repository_url = db.Column(db.String(2048))

    marshal_fields = {
        'name': fields.String,
        'uri': fields.Url('library_ep', absolute=True),
        'homepage_url': fields.String,
        'source_code_url': fields.String
    }


class ParadigmModel(db.Model):
    """
        A programming paradigm. For example, imperative or functional.
    """
    __tablename__ = 'paradigms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256), unique=True)
    is_visible = db.Column(db.Boolean(), default=False,
                           server_default="false", nullable=False)

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
    libraries = db.relationship('LibraryModel', backref='libraries',
                                lazy='dynamic')
    tutorials = db.relationship('TutorialModel', backref='tutorials',
                                lazy='dynamic')
    is_visible = db.Column(db.Boolean(), default=False,
                           server_default="false", nullable=False)

    marshal_fields = {
        'name': fields.String,
        'uri': fields.Url('pl_ep', absolute=True),
        'homepage_url': fields.String,
        'libraries': fields.Url('libraries_ep', absolute=True),
        #'tutorials': fields.Url('tutorials_ep', absolute=True),
    }


class TutorialModel(db.Model):
    """
        Represents an article or blog post with a tutorial for
        a specific programming language.
    """
    __tablename__ = 'tutorials'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256), unique=True)
    tutorial_url = db.Column(db.String(2048))
    language = db.Column(db.Integer,
                         db.ForeignKey('programming_languages.id'))
    is_visible = db.Column(db.Boolean(), default=False,
                           server_default="false", nullable=False)

    marshal_fields = {
        'name': fields.String,
        'uri': fields.Url('tutorial_ep', absolute=True),
        'tutorial_url': fields.String,
        'language': fields.Url('pl_ep', absolute=True),
    }

