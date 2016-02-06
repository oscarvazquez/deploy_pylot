"""
    System Core Model File

    Core Model file that all Models inherit from

    Gives a model access to the db object
    
"""
from flask import current_app
from flask.ext.bcrypt import Bcrypt
import models
from models import Post
import inspect

class Model(object):
    def __init__(self):
        self.db = current_app.db
        self.bcrypt = Bcrypt(current_app)
        self.post = Post
        self.models_name = {}
        for name, obj in inspect.getmembers(models):
        	if inspect.isclass(obj):
        		self.models_name[name] = obj