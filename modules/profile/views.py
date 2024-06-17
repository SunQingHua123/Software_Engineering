from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modules.profile.controllers import create_profile, get_profile_by_user_id, update_profile, delete_profile

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET'])
def view_profile():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    user_id = session['user_id']
    profile = get_profile_by_user_id(user_id)
    return render_template('profile.html', profile=profile)

@profile_bp.route('/profile/edit', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    user_id = session['user_id']
    if request.method == 'POST':
        nickname = request.form['nickname']
        avatar = request.form['avatar']
        contact_info = request.form['contact_info']
        update_profile(user_id, nickname, avatar, contact_info)
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile.view_profile'))
    profile = get_profile_by_user_id(user_id)
    return render_template('edit_profile.html', profile=profile)

@profile_bp.route('/profile/delete', methods=['POST'])
def delete_user_profile():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    user_id = session['user_id']
    delete_profile(user_id)
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    flash('Profile deleted successfully!', 'info')
    return redirect(url_for('users.login'))
