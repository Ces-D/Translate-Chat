from flask_socketio import send, join_room, leave_room, emit
from flask import redirect, flash, url_for, render_template, sessions
from flask_login import current_user, login_user, logout_user, login_required
import time

from TranslateChat import app, socketio, login_manager
from TranslateChat.forms import *
from TranslateChat.models import User


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# Predefined rooms
# TODO: Make this feature more dynamic
ROOMS = ["Lounge", "Memes"]


@app.route("/", methods=('GET', 'POST'))
def register():
    reg_form = RegistrationForm()

    # Update database if validation is successful
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hash password
        hashed_password = pbkdf2_sha256.hash(password)

        # Add username and password to DB
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        if user_object is None:
            return ("Login was not correct and you will need to fix this")
        login_user(user_object)
        return redirect(url_for('chat'))
        # TODO: Figure out what to do if login credentials not real

    return render_template("login.html", form=login_form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logout Successful')
    return redirect(url_for('login'))


# TODO: create logout button

@app.route("/chat", methods=['GET', 'POST'])
@login_required
def chat():
    return render_template('chat.html', username=current_user.username, rooms=ROOMS)


# Sockets Features


@socketio.on('incoming-msg')
def on_message(data):
    """Broadcast messages"""

    msg = data["msg"]
    username = data["username"]
    room = data["room"]
    # Set timestamp
    time_stamp = time.strftime('%b-%d %I:%M%p', time.localtime())
    send({"username": username, "msg": msg, "time_stamp": time_stamp}, room=room)


@socketio.on('join')
def on_join(data):
    """User joins a room"""

    username = data["username"]
    room = data["room"]
    join_room(room)

    # Broadcast that new user has joined
    send({"msg": username + " has joined " + room + "."}, room=room)


@socketio.on('leave')
def on_leave(data):
    """User leaves a room"""

    username = data['username']
    room = data['room']
    leave_room(room)
    send({"msg": username + " has left " + room}, room=room)