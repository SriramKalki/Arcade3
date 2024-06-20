from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Post
from forms import PostForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, date_posted=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('new_post.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)