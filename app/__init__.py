import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    FLASK_DEBUG=1

db = SQLAlchemy()
cors = CORS()

def create_app():
    app = Flask(__name__)
    cors.init_app(
        app,
        supports_credentials=True,
        resources={
            r"/*": {
                "origins": ["http://localhost:5173"]
            }
        },
    )
    db.init_app(app)
    app.config.from_object(Config)
    
    from .blueprint_api import api as a
    app.register_blueprint(a, url_prefix="/api")

    return app