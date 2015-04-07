from secret import SECRET_KEY

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://action:action@localhost:5432/blogful"
    DEBUG = True
    SECRET_KEY = SECRET_KEY

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://action:action@localhost:5432/blogful-test"
    DEBUG = False
    SECRET_KEY = "Not secret"

class TravisConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost:5432/blogful-test"
    DEBUG = False
    SECRET_KEY = "Not secret"

class LocalTestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://joe:joe@localhost:5432/blogful-test"
    DEBUG = False
    SECRET_KEY = "Not secret"
