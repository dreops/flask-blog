#import render_template function from the flask module
from application.forms import PostForm

from flask import render_template, redirect, url_for
# import the app object from the .application/_init__.py
from application import app, db
from application.models import Posts

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')


def home():
    def home():
        postData = Posts.query.first()
        return render_template('home.html', title='Home', post=postData)
    
@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            title = form.title.data,
            content = form.content.data
        )

        db.dession.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('post.html', title='Post', form=form)

