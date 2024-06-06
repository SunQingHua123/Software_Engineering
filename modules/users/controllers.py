import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from modules.users.models import User

def create_user(username, email, password, role):
    User.create(username, email, password, role)

def get_user_by_id(user_id):
    return User.get_by_id(user_id)

def get_all_users():
    return User.get_all()

def update_user(user_id, username, email, password, role):
    User.update(user_id, username, email, password, role)

def delete_user(user_id):
    User.delete(user_id)
