
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from config import Config
# from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_jwt_extended import JWTManager

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    # PORT = str(os.environ.get("DB_PORT"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    SECRET_KEY  = str(os.environ.get("SECRET_KEY"))
    CORS_HEADERS = 'Content-Type'
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    # SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024


# app.config.from_object(Config)
db = SQLAlchemy()
app = Flask(__name__)
jwt = JWTManager()
conf = Config()
def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)

def configure_database(app):
    @app.before_first_request
    def create_tables():
        db.create_all()
        
    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(apps):
    apps.config.from_object(conf)
    CORS(apps, resources={r"*": {"origins": "true"}})
    register_extensions(apps)
    configure_database(apps)
    
    from app.model import gambar, post, tanya, document, fatwa, komentar
    from app import routes
    return apps


