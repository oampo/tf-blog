from secret import SECRET_KEY

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog-development.db"
    DEBUG = True
    SECRET_KEY = SECRET_KEY

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog-testing.db"
    DEBUG = False
    SECRET_KEY = "Not secret"

