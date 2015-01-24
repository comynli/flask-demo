from flask.ext.sqlalchemy import SQLAlchemy

__author__ = 'xuemingli'

db = SQLAlchemy()

EXTENSIONS = (db, )