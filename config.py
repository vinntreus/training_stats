from os import environ

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ['SECRET_KEY']

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
