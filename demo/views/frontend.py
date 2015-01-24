from flask import Blueprint

__author__ = 'xuemingli'

frontend = Blueprint(__name__, 'frontend')


@frontend.route("/")
def index():
    return "hello world"