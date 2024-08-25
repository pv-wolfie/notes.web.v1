from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

#this file is a blueprint of our application, that includes urls to find the application

views = Blueprint('views', __name__)

# define a view, or a root in flask
@views.route('/') #whenever we go onto our url and type in /, we will run the home/main page of the app
@login_required # decorator to make sure that the user is logged in before they can access the home page
def home():
    return render_template("home.html", user = current_user) #reference current user to authenticate the user