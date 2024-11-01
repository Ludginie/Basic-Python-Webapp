#where we create our databse models
from . import db #importing from the CURRENT package(website folder) the db object
from flask_login import UserMixin
from sqlalchemy.sql import func  #gets current date and time
#class for note
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) #each note needs to have a primary key id, automatically generated
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())#we do not need to specify date field ourselves, date will be automatically added
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#foreign key referencing to the id of a user


class User(db.Model, UserMixin):
    #defining the schema
    id = db.Column(db.Integer, primary_key=True) #setting up unique identifier id
    email = db.Column(db.String(150), unique=True)#no user can have the same email as another user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')#tell flask and sqlalchemy, when we create a note add to the user's note relationship that note id, it will be a list storing all the notes the user owns
