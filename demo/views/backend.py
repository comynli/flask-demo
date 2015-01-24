from flask import Blueprint

__author__ = 'xuemingli'

backend = Blueprint(__name__, 'backend')


@backend.route("/")
def index():
    return 'admin'