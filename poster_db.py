from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

base = declarative_base()
engine = sa.create_engine('sqlite:///poster_bot.db')
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)

# after this:
# base == db.Model
# session == db.session
# other db.* values are in sa.*
# ie: old: db.Column(db.Integer,db.ForeignKey('s.id'))
#     new: sa.Column(sa.Integer,sa.ForeignKey('s.id'))
# except relationship, and backref, those are in orm
# ie: orm.relationship, orm.backref
# so to define a simple model


class Post(base):
    __tablename__ = 'posts'
    Rowid = sa.Column(sa.Integer, primary_key=True)
    fornecedor = sa.Column(sa.String(20), nullable=False)
    shortcode = sa.Column(sa.String(10), nullable=False)

    def __init__(self, fornecedor, shortcode):
        self.fornecedor = fornecedor
        self.shortcode = shortcode

    def __repr__(self):
        return f"Post('{self.fornecedor}', '{self.shortcode}')"


base.metadata.create_all()
