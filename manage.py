import os
from flask.ext.script import Manager
from demo.settings import create_app
from demo.ext import EXTENSIONS
from demo.mountpoints import MOUNT_POINTS
from demo import config
from demo.ext import db

__author__ = 'xuemingli'

env = os.environ.get("APP_ENV")
if env is None:
    env = 'DEV'

if env != 'PRD':
    env = 'DEV'

conf = getattr(config, '{}Config'.format(env))

app = create_app(conf, EXTENSIONS, MOUNT_POINTS)
manager = Manager(app)


@manager.command
def db_setup():
    """setup database"""
    db.create_all()


if __name__ == '__main__':
    manager.run(default_command='runserver')