import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from modules.logs.models import Log

def create_log(user_id, title, content):
    Log.create(user_id, title, content)

def get_log_by_id(log_id):
    return Log.get_by_id(log_id)

def get_all_logs_by_user_id(user_id):
    return Log.get_all_by_user_id(user_id)

def update_log(log_id, title, content):
    Log.update(log_id, title, content)

def delete_log(log_id):
    Log.delete(log_id)
