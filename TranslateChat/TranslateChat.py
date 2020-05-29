"""
Chat App that translates into the users chosen language. Every client chooses a language upon sign up and receives
and writes chosen messages in chosen language regardless of others language options
"""

from flask_socketio import SocketIO, send, join_room, leave_room
from flask import Flask, redirect
from TranslateChat.wtfforms_fields import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# Initialize Flask-SocketIO
socketio = SocketIO(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    return "Hello World"

@app.route("/submit", methods=('GET', 'POST'))
def submit():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect('/')

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

if __name__ == '__main__':
    socketio.run(app, debug=True)