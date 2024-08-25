from flask import Flask
from flask_sqlalchemy import SQLAlchemy #for the database

# Create a database object
db = SQLAlchemy() #database object
DB_NAME = "database.db"

# Create a Flask app and initialised it secret key
def create_app():
    # Create the flask app
    app = Flask(__name__)

    #encrypt the cookies and session data
    app.config['SECRET_KEY'] = 'abcdefghijklmnop'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #initailise the database
    db.init_app(app)

    # Import blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app

