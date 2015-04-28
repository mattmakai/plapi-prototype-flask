from plapi import db
from plapi.models import ParadigmModel, PLAPIResource, \
                         ProgrammingLanguageModel


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
    db.session.add(pl)
    db.session.commit()

    pl2 = ProgrammingLanguageModel()
    pl2.name = 'Swift'
    pl2.slug = 'swift'
    pl2.homepage_url = 'https://developer.apple.com/swift/'
    db.session.add(pl2)
    db.session.commit()

    prdgm1 = ParadigmModel()
    prdgm1.name = 'Imperative'
    prdgm1.slug = 'imperative'
    db.session.add(prdgm1)
    db.session.commit()


if __name__ == '__main__':
    load()
