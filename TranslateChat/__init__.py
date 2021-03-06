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

ENV = "dev"

if ENV == "dev":
    app.debug = "True"
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = LOCAL_DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
else:
    app.debug = "False"
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence deprecation warning

# Initialize Login Manager
login_manager = LoginManager(app)
login_manager.init_app(app)

# Initialize Flask-SocketIO
socketio = SocketIO(app)

# Create DB
db = SQLAlchemy(app)

from TranslateChat import routes
