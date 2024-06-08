import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from modules.users.models import User
from database import get_connection

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

def register_user(username, email, password, role):
    """
    用户注册
    参数:
        username (str): 用户名
        email (str): 邮箱
        password (str): 密码
        role (str): 用户角色，例如：admin, tutor, student
    返回:
        bool: 注册是否成功
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
                (username, email, password, role)
            )
        connection.commit()
        return True
    except Exception as e:
        print(f"注册失败：{e}")
        return False
    finally:
        connection.close()

def login_user(username, password):
    """
    用户登录
    参数:
        username (str): 用户名
        password (str): 密码
    返回:
        dict: 用户信息字典，如果登录失败则返回None
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE username = %s AND password = %s", 
                (username, password)
            )
            user = cursor.fetchone()
            if user:
                return {
                    'id': user['id'],
                    'username': user['username'],
                    'email': user['email'],
                    'role': user['role'],
                    'created_at': user['created_at']
                }
            else:
                return None
    except Exception as e:
        print(f"登录失败：{e}")
        return None
    finally:
        connection.close()


def get_user_by_email(email):
    return User.get_by_email(email)

def update_user_password(user_id, new_password):
    user = User.get_by_id(user_id)
    if user:
        User.update(user.id, user.username, user.email, new_password, user.role)
        return True
    return False