from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note
from . import db
import json

#this file is a blueprint of our application, that includes urls to find the application

views = Blueprint('views', __name__)

# define a view, or a root in flask
@views.route('/', methods=['GET', 'POST']) #whenever we go onto our url and type in /, we will run the home/main page of the app
@login_required # decorator to make sure that the user is logged in before they can access the home page
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added!', category='success')
    return render_template("home.html", user = current_user) #reference current user to authenticate the user

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) #load the json data from the request and turn it into a python dictionary
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note: #check if the note exists
        if note.user_id == current_user.id: #check if the user is the owner of the note
            db.session.delete(note) #delete the note
            db.session.commit() #commit the changes to the database
            return jsonify({}) #return an empty json object
