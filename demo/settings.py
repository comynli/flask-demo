from flask import Flask

__author__ = 'xuemingli'


APP_NAME = 'demo'


def create_app(cfg=None, extensions=None, mountpoints=None):
    app = Flask(APP_NAME)
    if cfg:
        app.config.from_object(cfg)
    if extensions:
        configure_ext(app, extensions)
    if mountpoints:
        configure_blueprints(app, mountpoints)
    return app


def configure_ext(app, extensions):
    for ext in extensions:
        ext.init_app(app)


def configure_blueprints(app, mountpoints):
    for module, url_prefix in mountpoints:
        app.register_blueprint(module, url_prefix=url_prefix)
    return app

