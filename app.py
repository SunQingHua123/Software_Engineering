import os
from flask import Flask, render_template, redirect, url_for, session
from database.init_db import init_db
from modules.users.views import users_bp
from modules.books.views import books_bp
from modules.messages.views import messages_bp
from modules.friendships.views import friendships_bp
from modules.profile.views import profile_bp
from modules.logs.views import logs_bp
from modules.booklist.views import booklist_bp
from modules.reviews.views import reviews_bp
from modules.circles.views import circles_bp


# 初始化 Flask 应用
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)

# 注册蓝图
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(messages_bp, url_prefix='/messages')
app.register_blueprint(friendships_bp, url_prefix='/friendships')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(logs_bp, url_prefix='/logs')
app.register_blueprint(booklist_bp, url_prefix='/booklists')
app.register_blueprint(reviews_bp, url_prefix='/reviews')
app.register_blueprint(circles_bp, url_prefix='/circles')


# 初始化数据库
init_db()

# 首页路由
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    return render_template('index.html')

# 关于页面路由
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
