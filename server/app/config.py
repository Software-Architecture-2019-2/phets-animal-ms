import os


class Config(object):
    DEBUG = False


class Configdb(Config):
    DB_CONFIG = {
        "con": "mysql+pymysql",
        "user": os.environ.get('DATABASE_USER') or "animalUser",
        "pass": os.environ.get('DATABASE_PASS') or "password",
        "uri": os.environ.get('DATABASE_URI') or "0.0.0.0:3003",
        "name": os.environ.get('DATABASE_NAME') or "animals"
    }
    SQLALCHEMY_DATABASE_URI = '{con}://{user}:{pass}@{uri}/{name}'.format(
        **DB_CONFIG)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
