from flask import Blueprint

#this file is a blueprint of our application, that includes urls to find the application

views = Blueprint('views', __name__)

# define a view, or a root in flask
@views.route('/') #whenever we go onto our url and type in /, we will run the home/main page of the app
def home():
    return "<h1>Test</h1>"