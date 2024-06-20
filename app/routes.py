from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

posts = []

@main.route('/')
def index():
    return render_template('index.html', posts=posts)

@main.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('main.index'))
    return render_template('create_post.html')