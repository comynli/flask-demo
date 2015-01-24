from ..ext import db

__author__ = 'xuemingli'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), unique=True, nullable=False)