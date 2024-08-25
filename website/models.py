from . import db #import db from current package
from flask_login import UserMixin #for the user object
from sqlalchemy.sql import func #for the date object

# Create a notes class
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) #id is the primary key
    data = db.Column(db.String(10000)) #data is a string with a max length of 10000
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #date is a datetime object

    '''
    when you have a one-to-many relationship you have one object that has many children now in this case we have one user that has
    many notes so what we do is we store a foreign key on the child objects that reference the parent object so now every time we 
    have a note we can figure out which user created it by looking at the user id and again this db.foreign key enforces that we 
    must give a valid user id to this object otherwise we cannot create it because we have a relationship a relationship between 
    the user and notes to identify and link the user to the notes through a foreign key relationship
    '''

    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #user_id is a foreign key to the user table

# Create a user class
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #id is the primary key
    email = db.Column(db.String(150), unique=True) #email is unique to users
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #relationship between the user and notes
    