import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, ORS_API_KEY
from .commands import register_commands as _register_commands


def create_app():
    """
    Create the flask application with IoC.

    :return:
    """
    app = Flask(__name__)
    register_configuration(app)
    db = register_database(app)
    register_commands(app, db)

    return app, db


def register_configuration(app):
    """
    Register the base configuration for the application.

    :param app:
    :return:
    """
    app.config[SQLALCHEMY_DATABASE_URI] = '{protocol}://{user}:{password}@{host}/{db}'.format(
        protocol=os.environ.get('DB_PROTOCOL'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        host=os.environ.get('DB_HOST'),
        db=os.environ.get('DB_DB')
    )
    app.config[SQLALCHEMY_TRACK_MODIFICATIONS] = False
    app.config[ORS_API_KEY] = os.environ.get('ORS_API_KEY')


def register_database(app):
    """
    Register the database.

    :param app:
    :return:
    """
    return SQLAlchemy(app)


def register_commands(app, db):
    """
    Register the commands.

    :param app:
    :param db:
    :return:
    """
    _register_commands(app, db)
