import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    DEBUG = True
    CSRF_ENABLED = True


DB_CONFIG = {
    "user": "animalUser",
    "pass": "password",
    "uri": "0.0.0.0",
    "name": "animals"
}

class Configdb(Config):
    # DB_USER = os.environ.get('DATABASE_USER')
    # DB_PASS = os.environ.get('DATABASE_PASS')
    # DB_URI = os.environ.get('DATABASE_URI')
    # DB_NAME = os.environ.get('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pass}@{uri}/{name}'.format(**DB_CONFIG)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
