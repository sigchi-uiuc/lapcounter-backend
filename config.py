import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aJMRa9Tw81so2ncyhLvDED6prS'
    SQLALCHEMY_DATABASE_URI = os.environ['postgres://igsusmnkuuuiff:aJMRa9Tw81so2ncyhLvDED6prS@ec2-107-21-222-62.compute-1.amazonaws.com:5432/dflphcsocv57hu']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True