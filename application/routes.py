#import render_template function from the flask module
from flask import render_template, redirect, url_for
# import the app object from the .application/_init__.py
from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, RegistrationForm

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
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
    

        user = Users(email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()
    
        return redirect(url_for('post'))
    return render_template('register.html', title='Register', form=form)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_onsubmit():
        postData = Posts(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            title=form.tite.data,
            content=form.content.data
        )
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))
    else:
            print(form.errors)
    return render_template('post.html', title='Post', form=form)
