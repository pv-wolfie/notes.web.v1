from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

#hashing function is a one way function such that it does not have an inverse now what does that mean well if we have a function x maps to y
#this is so that we arn't storing the password in plain text in the database so that if the database is compromised the passwords are not for security measures



#this file is a blueprint of our application, that includes urls to find the application
auth = Blueprint('auth', __name__)

### NOTES ###
# methods:
#   when you go to a url you get a GET request
#   when you submit a form you get a POST request

# def login, logout, signout
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #validate the email and password in the database
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) #remember the fact that the user is logged in until the user logs out or the session expires
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist. Incorrect email or Sign Up.', category='error')


    return render_template("login.html", user = current_user) #reference current user to authenticate the user

@auth.route('/logout')
@login_required # decorator to make sure that the user is logged in before they can log out
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists with this email already exists!', category='error')
        
        #validation
        if len(email) < 4 :
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # creat a new user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256')) #pbkdf2:sha256 is a hashing algorithm
            db.session.add(new_user) # add the new user to the database
            db.session.commit() # commit the changes to the database
            login_user(user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home')) #redirect us to another page

    return render_template("signup.html", user = current_user)