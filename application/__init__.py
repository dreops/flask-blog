from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv
from flask_login import LoginManager

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes