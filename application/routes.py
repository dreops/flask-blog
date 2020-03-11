#import render_template function from the flask module
from flask import render_template, redirect, url_for
# import the app object from the .application/_init__.py
from application import app, db

from application.models import Posts

from application.forms import PostForm

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.first()
    return render_template('home.html', title='Home', post=postData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/post')
def post():
    return render_template('post.html', title='Post')
