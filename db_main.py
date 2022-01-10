import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy import create_engine  # Todas as operacoes nas tables


BASE = declarative_base()
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
CONNECTION_STRING = 'sqlite:///' + os.path.join(BASE_DIR, 'poster.db')
ENGINE = create_engine(CONNECTION_STRING, echo=True)

newsession = sessionmaker()
local_session = newsession(bind=ENGINE)


class Post(BASE):
    __tablename__ = 'posts'

    Rowid = Column(Integer(), primary_key=True)
    fornecedor = Column(String(20), nullable=False)
    shortcode = Column(String(10), nullable=False, unique=True)

    def __init__(self, fornecedor, shortcode):
        self.fornecedor = fornecedor
        self.shortcode = shortcode

    def __repr__(self):
        return f"Post(' fornecedor: {self.fornecedor}', shortcode: '{self.shortcode}')"

    @classmethod
    def find_shortcode(cls, shortcode):
        return local_session.query(Post).filter(Post.shortcode == shortcode).first()

    @classmethod
    def add(cls, fornecedor, shortcode):
        shortcodetoadd = Post(fornecedor, shortcode)
        local_session.add(shortcodetoadd)
        local_session.commit()

# INICIA AS TABLES
# BASE.metadata.create_all(ENGINE)
