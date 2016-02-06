""" 
    System Initialization File

    Loads initializers for configurations, database, and routes and creates the flask application
"""
from flask import Flask
import os
from app.config import database as database_config
from app.config import routes

from system.init.configuration import initialize_config
from system.init.database import initialize_db
from system.init.routes import initialize_routes

import sqlalchemy


def initialize_app():
    instance_path = os.path.abspath(os.path.dirname(__file__) + '/../..')
    template_folder = os.path.join(instance_path, 'app/views')
    static_folder = os.path.join(instance_path, 'app/static')

    app = Flask('app', static_folder=static_folder, template_folder=template_folder, instance_path=instance_path)

    initialize_config(app)
    initialize_db(app)
    initialize_routes(app)

    return app

def _get_config(env):
    return {
        'DEVELOPMENT': database_config.DevelopmentDBConfig,
        'STAGING': database_config.StagingDBConfig,
        'PRODUCTION': database_config.ProductionDBConfig,
    }.get(env, database_config.DevelopmentDBConfig)

def create_database(app, db_name):
    config = _get_config(os.getenv('PYLOT_ENV', 'DEVELOPMENT'))
    os.environ['DATABASE_URL'] = "mysql://" + str(config.DB_USERNAME) + ":" + str(config.DB_PASSWORD) + "@127.0.0.1:" + str(config.DB_PORT)
    os.environ['DATABASE_NAME'] = db_name
    engine = sqlalchemy.create_engine(os.environ['DATABASE_URL'])
    # engine = sqlalchemy.create_engine("mysql://root:root@127.0.0.1:8889")
    os.environ['SQLAlchemy_DATABASE_URI'] = os.environ['DATABASE_URL'] + "/" + db_name
    engine.execute("CREATE DATABASE {}".format(db_name))
    engine.execute("USE {}".format(db_name))
    app.config['SQLAlchemy_DATABASE_URI'] = os.environ['SQLAlchemy_DATABASE_URI']
