"""
Chat App that translates into the users chosen language. Every client chooses a language upon sign up and receives
and writes chosen messages in chosen language regardless of others language options
"""

from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Initialize Flask-SocketIO
socketio = SocketIO(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

#Initialize DB
db = SQLAlchemy()


from TranslateChat import routes