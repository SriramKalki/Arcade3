from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Post, db
from .forms import PostForm
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@main.route('/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, date_posted=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('new_post.html', form=form)