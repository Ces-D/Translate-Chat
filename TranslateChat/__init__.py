"""
Chat App that translates into the users chosen language. Every client chooses a language upon sign up and receives
and writes chosen messages in chosen language regardless of others language options
"""

from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from secrets import *
import psycopg2


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #silence deprecation warning


# Initialize Flask-SocketIO
socketio = SocketIO(app)

# Initialize Login Manager
login_manager = LoginManager(app)

# Initialize DB
db = SQLAlchemy(app)


from TranslateChat import routes