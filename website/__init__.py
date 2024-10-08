from flask import Flask
from flask_sqlalchemy import SQLAlchemy #for the database
from os import path #for the path of the database
from flask_login import LoginManager

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

    from .models import User, Note
    #check if we have created the database before the script is run
    create_database(app)

    # Create a login manager object
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #redirect the user to the login page if they are not logged in
    login_manager.init_app(app) 

    @login_manager.user_loader
    def load_user(id): # tell flask how we load a user
        return User.query.get(int(id)) #get the user by the id, by default look for the primary key

    return app

# Check if the database already exits if not then 
# create it because otherwise if it does exist we don't want to override 
# it because it contains data

# Create the database
def create_database(app):
    #if the database does not exist create it
    if not path.exists('website/' + DB_NAME): #check if the database exists
        with app.app_context():
            db.create_all() #create the database for the app and tell sqlalchemy which app to create the database for
        print('Created Database!') 