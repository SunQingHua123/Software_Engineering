from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modules.logs.controllers import create_log, get_log_by_id, get_all_logs_by_user_id, update_log, delete_log

logs_bp = Blueprint('logs', __name__)

@logs_bp.route('/logs', methods=['GET'])
def view_logs():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    user_id = session['user_id']
    logs = get_all_logs_by_user_id(user_id)
    return render_template('logs.html', logs=logs)

@logs_bp.route('/logs/create', methods=['GET', 'POST'])
def create_log_view():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        create_log(session['user_id'], title, content)
        flash('Log created successfully!', 'success')
        return redirect(url_for('logs.view_logs'))
    return render_template('create_log.html')

@logs_bp.route('/logs/edit/<int:log_id>', methods=['GET', 'POST'])
def edit_log(log_id):
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        update_log(log_id, title, content)
        flash('Log updated successfully!', 'success')
        return redirect(url_for('logs.view_logs'))
    log = get_log_by_id(log_id)
    return render_template('edit_log.html', log=log)

@logs_bp.route('/logs/delete/<int:log_id>', methods=['POST'])
def delete_log_view(log_id):
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    delete_log(log_id)
    flash('Log deleted successfully!', 'info')
    return redirect(url_for('logs.view_logs'))
