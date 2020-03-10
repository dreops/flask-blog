# import Flask class from the flask module
from flask import Flask

# craete a new instance of Flask and store it in app
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#app.config ['SQLALCHEMY_DATABASE_URI']= 'pp.config['SQLALCHEMY_DATABASE_URI']=pymysql+mysql://root:root@ 35.197.228.134 /flask_blog' - COMMENTED OUT BECAUSE NOT RIGHT??


app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://root:root@35.197.228.134/Flask_blog')

#str(os.getenv('DATABASE_URI')) This was on the other

db = SQLAlchemy(app)

# import the ./application/routes.py file
from application import routes

FROM os import getenv

#app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')

get env('SECRET_KEY')
getenv ('DATABASE_URI')