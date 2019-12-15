import os


class Config(object):
    DEBUG = False


class Configdb(Config):
    DB_CONFIG = {
        "con": "mysql+pymysql",
        "user": os.environ.get('DATABASE_USER') or "animalUser",
        "pass": os.environ.get('DATABASE_PASS') or "password",
        "host": os.environ.get('DATABASE_HOST') or "0.0.0.0",
        "port": os.environ.get('DATABASE_PORT') or "3003",
        "name": os.environ.get('DATABASE_NAME') or "animals"
    }
    SQLALCHEMY_DATABASE_URI = '{con}://{user}:{pass}@{host}:{port}/{name}'.format(
        **DB_CONFIG)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
