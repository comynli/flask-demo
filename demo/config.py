__author__ = 'xuemingli'


class Config:
    DEBUG = True


class DEVConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


class PRDConfig(Config):
    pass