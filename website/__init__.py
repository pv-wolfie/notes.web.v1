from flask import Flask

# Create a Flask app and initialised it secret key
def create_app():
    # Create the flask app
    app = Flask(__name__)

    #encrypt the cookies and session data
    app.config['SECRET_KEY'] = 'abcdefghijklmnop'

    return app

