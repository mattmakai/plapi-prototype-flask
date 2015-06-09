from plapi import db
from plapi.models import (ParadigmModel, PLAPIResource, TutorialModel,
                         ProgrammingLanguageModel, LibraryModel, )


def load():
    """
        Temporary function to load basic testing data.
    """
    pr = PLAPIResource()
    pr.name = 'Programming Languages'
    pr.uri = 'programming-languages'
    db.session.add(pr)
    db.session.commit()

    pd = PLAPIResource()
    pd.name = 'Paradigms'
    pd.uri = 'paradigms'
    db.session.add(pd)
    db.session.commit()

    pl = ProgrammingLanguageModel()
    pl.name = 'Python'
    pl.slug = 'python'
    pl.homepage_url = 'https://www.python.org/'
    pl.is_visible = True
    db.session.add(pl)
    db.session.commit()

    pl2 = ProgrammingLanguageModel()
    pl2.name = 'Swift'
    pl2.slug = 'swift'
    pl2.homepage_url = 'https://developer.apple.com/swift/'
    pl2.is_visible = True
    db.session.add(pl2)
    db.session.commit()

    prdgm1 = ParadigmModel()
    prdgm1.name = 'Imperative'
    prdgm1.slug = 'imperative'
    prdgm1.is_visible = True
    db.session.add(prdgm1)
    db.session.commit()

    lib = LibraryModel()
    lib.name = 'Django'
    lib.slug = 'django'
    lib.is_visible = True
    lib.language = pl.id
    lib.homepage_url = 'https://www.djangoproject.com/'
    lib.source_code_url = 'https://github.com/django/django'
    db.session.add(lib)
    db.session.commit()

    tut = TutorialModel()
    tut.name = 'Choose Your Own Adventure Presentations'
    tut.slug = 'choose-your-own-adventure-presentations'
    tut.is_visible = True
    tut.language = pl.id
    tut.tutorial_url = 'https://www.twilio.com/blog/2014/11/choose-your-own-adventure-presentations-with-reveal-js-python-and-websockets.html'
    db.session.add(tut)
    db.session.commit()


if __name__ == '__main__':
    load()
