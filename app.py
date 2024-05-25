import os
from modules.books.views import books_bp
from flask import Flask, render_template
from database.init_db import init_db

# 初始化 Flask 应用
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)

# 注册蓝图
app.register_blueprint(books_bp, url_prefix='/books')

# 初始化数据库
init_db()

# 首页路由
@app.route('/')
def index():
    # 在这里可以添加渲染首页的逻辑
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
