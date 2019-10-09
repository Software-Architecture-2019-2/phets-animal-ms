from flask import Flask
from app.config import Configdb
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from datetime import date
from app.server import run

app = Flask(__name__)

app.config.from_object(Configdb)
db = SQLAlchemy(app)

ma = Marshmallow(app)

api = Api(app)

run()
