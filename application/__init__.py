# import Flask class from the flask module
from flask import Flask
from flask_bcrypt import Bcrypt
from os import getenv

# craete a new instance of Flask and store it in app
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
bcrypt = Bcrypt(app)


#app.config ['SQLALCHEMY_DATABASE_URI']= 'pp.config['SQLALCHEMY_DATABASE_URI']=pymysql+mysql://root:root@ 35.197.228.134 /flask_blog' - COMMENTED OUT BECAUSE NOT RIGHT??


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

#str(os.getenv('DATABASE_URI')) This was on the other

db = SQLAlchemy(app)

# import the ./application/routes.py file
from application import routes


# Extra Notes:
#app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
