from flask import Blueprint

#this file is a blueprint of our application, that includes urls to find the application

auth = Blueprint('auth', __name__)

#def login, logout, signout
@auth.route('/login')
def login():
    return "<h1>Login</h1>"

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up')
def signout():
    return "<h1>Sign Up</h1>"