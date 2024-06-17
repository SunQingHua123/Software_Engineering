import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from flask import Blueprint, render_template, request, redirect, url_for
from modules.circles.controllers import create_circle, get_circle_by_id, update_circle, delete_circle, add_member_to_circle, remove_member_from_circle, get_circles

circles_bp = Blueprint('circles', __name__, template_folder='../../templates')

@circles_bp.route('/')
def index():
    circles = get_circles()  # 获取所有圈子的列表
    return render_template('circle_list.html', circles=circles)

@circles_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        user_id = request.form.get('user_id')  # 实际应用中应从session或token中获取
        if not name or not description or not user_id:
            return "Error: All fields are required", 400
        circle_id = create_circle(name, description, user_id)
        return redirect(url_for('circles.index'))
    return render_template('circle_form.html', form_title='创建圈子', circle=None)

@circles_bp.route('/edit/<int:circle_id>', methods=['GET', 'POST'])
def edit(circle_id):
    circle = get_circle_by_id(circle_id)
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        if not name or not description:
            return "Error: All fields are required", 400
        update_circle(circle_id, name, description)
        return redirect(url_for('circles.index'))
    return render_template('circle_form.html', form_title='编辑圈子', circle=circle)

@circles_bp.route('/delete/<int:circle_id>', methods=['POST'])
def delete(circle_id):
    delete_circle(circle_id)
    return redirect(url_for('circles.index'))

@circles_bp.route('/add_member', methods=['POST'])
def add_member():
    circle_id = request.form.get('circle_id')
    user_id = request.form.get('user_id')
    role = request.form.get('role', 'member')
    if not circle_id or not user_id:
        return "Error: Circle ID and User ID are required", 400
    add_member_to_circle(circle_id, user_id, role)
    return redirect(url_for('circles.index'))

@circles_bp.route('/remove_member', methods=['POST'])
def remove_member():
    circle_id = request.form.get('circle_id')
    user_id = request.form.get('user_id')
    if not circle_id or not user_id:
        return "Error: Circle ID and User ID are required", 400
    remove_member_from_circle(circle_id, user_id)
    return redirect(url_for('circles.index'))
