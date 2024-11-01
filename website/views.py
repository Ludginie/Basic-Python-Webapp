#store standard roots fro website, home page, anythign the user can naviagte to

from flask import Blueprint, render_template, request, flash, jsonify #it is the blueprint for our application
from flask_login import  login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint ('views', __name__) #don't need to name it 'views', but easier to

#to define a view/root
@views.route('/', methods=['GET', 'POST'])#define the url, whenerver we pyut a / in our url, it will go home
@login_required #add a login required decorator to home page, cannot get to home page unless u log in
def home():
    if request.method =='POST':
        note = request.form.get('note')
        if len(note) < 1:
                flash('Note is too short', category='error')
        else:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='success')

    return render_template("home.html", user=current_user)#in our template we are going to be able to reference the current user

@views.route('/delete-note', methods=['POST'])
def delete_note():
       #take the string from request data, the string being noteid from indexjs and turns into a python dictionary object
      note =json.loads(request.data)
      noteId = note['noteId']
      note = Note.query.get(noteId)#accesses primary key
      if note: #if note exit
            if note.user_id == current_user.id : #if user signed in owns this note
                db.session.delete(note) #we will delete the note
                db.session.commit()

      return jsonify({}) #return empty response