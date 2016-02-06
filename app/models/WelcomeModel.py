""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    """
    def add_post(self):
        Post = self.models_name['Post']
        post = Post('oscar', 'this is something exciting title')
        self.db.session.add(post)
        self.db.session.commit()
        return post
    def grab_posts(self):
        Post = self.db.session.execute("SELECT * FROM post where id = :user_id", {'user_id': 10})
        return Post
    """
    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """

    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """
