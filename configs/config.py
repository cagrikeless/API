from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from flask_marshmallow import Marshmallow
from local_settings import postgresql as settings
from sqlalchemy_utils import database_exists, create_database 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:PASSWORD@HOST:PORT/DBNAME"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine(settings['pguser'],
          settings['pgpasswd'],
          settings['pghost'],
          settings['pgport'],
          settings['pgdb'])


Session = sessionmaker(bind=engine)
session = Session()