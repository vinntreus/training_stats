from os import environ

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
