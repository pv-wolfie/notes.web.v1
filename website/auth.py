from flask import Blueprint, render_template

#this file is a blueprint of our application, that includes urls to find the application

auth = Blueprint('auth', __name__)

#def login, logout, signout
@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up')
def signout():
    return render_template("signup.html")