from . import db


class ProgrammingLanguageModel(db.Model):
    """
        Represents a single programming language and information
        about it.
    """
    __tablename__ = 'programming_languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256), unique=True)
    homepage_url = db.Column(db.String(2048))


