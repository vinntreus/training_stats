from os import environ


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_SEND_PASSWORD_CHANGED_EMAIL = False
    USER_SEND_REGISTERED_EMAIL = False
    USER_SEND_USERNAME_CHANGED_EMAIL = False
    USER_ENABLE_LOGIN_WITHOUT_CONFIRM_EMAIL = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
