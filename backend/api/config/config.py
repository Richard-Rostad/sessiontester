class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://sessions:sessions@host.docker.internal:3306/sessiondb'
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://sessions:sessions@host.docker.internal:3306/sessiondb'
    SQLALCHEMY_ECHO = False
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sessions:sessions@host.docker.internal:3306/sessiondb'
    SQLALCHEMY_ECHO = False