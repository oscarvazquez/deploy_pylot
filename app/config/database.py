"""
    Database Specific Configuration File
"""
""" Put Generic Database Configurations here """
import os

class DBConfig(object):
    """ DB_ON must be True to use the DB! """
    DB_ON = True
    DB_DRIVER = 'mysql'
    DB_ORM = True
    if "SQLAlchemy_DATABASE_URI" in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ['SQLAlchemy_DATABASE_URI']
        print SQLALCHEMY_DATABASE_URI

""" Put Development Specific Configurations here """
class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'new_oscar'
    DB_HOST = 'localhost'
    DB_PORT = 3306
    """ unix_socket is used for connecting with MAMP. Take this out if you aren't using MAMP """
    DB_OPTIONS = {
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
    }

""" Put Staging Specific Configurations here """
class StagingDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'mydb'
    DB_HOST = 'localhost'

""" Put Production Specific Configurations here """
class ProductionDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'mydb'
    DB_HOST = 'localhost'
