from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modules.users.controllers import login_user, register_user
from modules.users.models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login_user(username, password)
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash('登录成功', 'success')
            return redirect(url_for('index'))
        else:
            flash('登录失败，请检查用户名和密码', 'danger')
    return render_template('login.html')

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']  # 用户角色，例如：admin, tutor, student
        if register_user(username, email, password, role):
            flash('注册成功，请登录', 'success')
            return redirect(url_for('users.login'))
        else:
            flash('注册失败，请重试', 'danger')
    return render_template('register.html')

@users_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    flash('您已成功登出', 'info')
    return redirect(url_for('users.login'))
