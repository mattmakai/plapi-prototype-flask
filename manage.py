import os

from plapi import app, db
from plapi.models import PLAPIResource, ProgrammingLanguageModel, LibraryModel
from flask.ext.script import Manager, Shell

manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, PLAPIResource=PLAPIResource,
                ProgrammingLanguageModel=ProgrammingLanguageModel,
                LibraryModel=LibraryModel)


manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def syncdb():
    db.create_all()


@manager.command
def backupdb():
    for r in PLAPIResource.query.all():
        print r.generate_curl()


@manager.command
def runserver():
    app.run("0.0.0.0", port=5001, debug=True)


if __name__ == '__main__':
    manager.run()
