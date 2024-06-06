import os
from modules.books.views import books_bp
from flask import Flask, render_template, redirect, url_for, session
from database.init_db import init_db
from modules.users.views import users_bp

# 初始化 Flask 应用
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)

# 注册蓝图
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(books_bp, url_prefix='/books')

# 初始化数据库
init_db()

# 首页路由
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
