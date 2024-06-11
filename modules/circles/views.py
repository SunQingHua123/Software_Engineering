from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from yourapp.controllers.circles_controller import (
    create_circle, get_circle_by_id, update_circle, delete_circle,
    add_member_to_circle, remove_member_from_circle,
    create_discussion, delete_discussion
)

circles_bp = Blueprint('circles', __name__)

@circles_bp.route('/circles/create', methods=['GET', 'POST'])
def create_circle_view():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        creator_id = session.get('user_id')  # 假设用户ID已经保存在session中
        if create_circle(name, description, creator_id):
            flash('圈子创建成功', 'success')
        else:
            flash('创建失败', 'danger')
        return redirect(url_for('circles.list_circles'))
    return render_template('create_circle.html')

@circles_bp.route('/circles/delete/<int:circle_id>', methods=['POST'])
def delete_circle_view(circle_id):
    if delete_circle(circle_id):
        flash('圈子删除成功', 'success')
    else:
        flash('删除失败', 'danger')
    return redirect(url_for('circles.list_circles'))

@circles_bp.route('/circles/add_member', methods=['POST'])
def add_member_view():
    circle_id = request.form['circle_id']
    user_id = request.form['user_id']
    if add_member_to_circle(circle_id, user_id):
        flash('成员添加成功', 'success')
    else:
        flash('添加失败', 'danger')
    return redirect(url_for('circles.circle_details', circle_id=circle_id))

@circles_bp.route('/circles/remove_member', methods=['POST'])
def remove_member_view():
    circle_id = request.form['circle_id']
    user_id = request.form['user_id']
    if remove_member_from_circle(circle_id, user_id):
        flash('成员移除成功', 'success')
    else:
        flash('移除失败', 'danger')
    return redirect(url_for('circles.circle_details', circle_id=circle_id))

@circles_bp.route('/discussions/create', methods=['GET', 'POST'])
def create_discussion_view():
    if request.method == 'POST':
        circle_id = request.form['circle_id']
        creator_id = session.get('user_id')
        topic = request.form['topic']
        content = request.form['content']
        if create_discussion(circle_id, creator_id, topic, content):
            flash('讨论创建成功', 'success')
        else:
            flash('创建失败', 'danger')
        return redirect(url_for('circles.circle_details', circle_id=circle_id))
    return render_template('create_discussion.html')

@circles_bp.route('/discussions/delete/<int:discussion_id>', methods=['POST'])
def delete_discussion_view(discussion_id):
    if delete_discussion(discussion_id):
        flash('讨论删除成功', 'success')
    else:
        flash('删除失败', 'danger')
    return redirect(url_for('circles.circle_details', circle_id=request.form['circle_id']))
