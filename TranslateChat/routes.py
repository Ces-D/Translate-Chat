from flask_socketio import send, join_room, leave_room, emit
from flask import redirect, flash, url_for, render_template
from flask_login import current_user, login_user, logout_user, login_required
from TranslateChat import app, socketio, db
from TranslateChat.forms import RegistrationForm, LoginForm
from TranslateChat.models import User


@app.route("/", methods=('GET', 'POST'))
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Add user to DB
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB"

    return render_template('register.html',form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        flash('Log in Successful')
        return redirect(url_for('chat'))
    return redirect(url_for('index'))


# TODO: create 'login.html'

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logout Succesful')
    return redirect(url_for('login'))


# TODO: Do we need logout.html

@app.route("/chat", methods=['GET', 'POST'])
@login_required
def chat():
    if not current_user.is_authenticated:
        flash('Please login.', 'danger')
        return redirect(url_for('login'))
    return render_template('chat.html')
# TODO: create chat.html


# Rooms
# group users into subsets that can be addressed together
# users receive messages from the room or rooms they are in, but not from other rooms where other users are
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)


# Receiving Messages
# messages are received by both parties as events
# the server needs to register handlers for these events, similarly to how routes are handled by view functions.
@socketio.on('my event')
# The message data for these events can be string, bytes, int, or JSON
def handle_my_custom_event(json):
    print('received json: ' + str(json))


# Sending Messages
@socketio.on('message')
def message(data):
    send(data)
    emit('some-event', "this is a custom event message")
