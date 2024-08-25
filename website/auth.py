from flask import Blueprint, render_template, request, flash

#this file is a blueprint of our application, that includes urls to find the application

auth = Blueprint('auth', __name__)

### NOTES ###
# methods:
#   when you go to a url you get a GET request
#   when you submit a form you get a POST request

# def login, logout, signout
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def signout():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #validation
        if len(email) < 4 :
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to database
            flash('Account Created!', category='success')

    return render_template("signup.html")