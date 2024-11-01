#authentification file 

#blueprint for our application, get info that was sent in form, message flashing
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #way to secure password, never store password in plain text
#hashing function is a fucntion that has no inverse
from . import db #import db from init
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint ('auth', __name__) #don't need to name it 'auth', but easier to

@auth.route('/login', methods=['GET', 'POST']) #able to accept get and post request
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #check if user email is valid
        user = User.query.filter_by(email=email).first() #loosing for specific item in user data base, in this case looking by first person w that email
        if user: #check if password that is typed in is equal to the hash on the server
            if check_password_hash(user.password, password): #if hashes are the same
                flash ('Logged in successfully!',category='success')
                login_user(user, remember=True) #this is going to actually login the user
                return redirect(url_for('views.home'))
            else:
                flash ('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')


    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required #this makes sure we cannot access this route unless user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',  methods=['GET', 'POST'])
def sign_up():
    #differentiate between get and post request
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash ('Email already exists.', category='error')

        if len(email) < 4: #if email is less than 4 characters, tell user there is an issue
            flash('Email must be greater than 3 characters.', category='error' ) #can name category whatever
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error' ) #can name category whatever
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error' ) #can name category whatever
        elif len(password1) < 7 :
            flash('Password must be at LEAST  7 characters.', category='error' ) #can name category whatever
        else:
            #add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256')) #sha256 is a hashing algorithm
            db.session.add(new_user) #add the new user tot he database
            db.session.commit() # we made changes, update the database
            login_user(user, remember=True)
            flash ('Account Created!', category='success' )
            return redirect(url_for('views.home')) #redirect to home page after account is created


    return render_template("sign_up.html", user=current_user)
