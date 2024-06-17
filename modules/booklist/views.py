from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modules.booklist.controllers import create_booklist, get_booklist_by_id, get_all_booklists_by_user_id, update_booklist, delete_booklist

booklist_bp = Blueprint('booklist', __name__)

@booklist_bp.route('/booklists', methods=['GET'])
def view_booklists():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    user_id = session['user_id']
    booklists = get_all_booklists_by_user_id(user_id)
    return render_template('booklists.html', booklists=booklists)

@booklist_bp.route('/booklists/create', methods=['GET', 'POST'])
def create_booklist_view():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        create_booklist(session['user_id'], title, author)
        flash('Booklist created successfully!', 'success')
        return redirect(url_for('booklist.view_booklists'))
    return render_template('create_booklist.html')

@booklist_bp.route('/booklists/edit/<int:booklist_id>', methods=['GET', 'POST'])
def edit_booklist(booklist_id):
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        update_booklist(booklist_id, title, author)
        flash('Booklist updated successfully!', 'success')
        return redirect(url_for('booklist.view_booklists'))
    booklist = get_booklist_by_id(booklist_id)
    return render_template('edit_booklist.html', booklist=booklist)

@booklist_bp.route('/booklists/delete/<int:booklist_id>', methods=['POST'])
def delete_booklist_view(booklist_id):
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    delete_booklist(booklist_id)
    flash('Booklist deleted successfully!', 'info')
    return redirect(url_for('booklist.view_booklists'))
