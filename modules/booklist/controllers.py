import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from modules.booklist.models import Booklist

def create_booklist(user_id, title, author):
    Booklist.create(user_id, title, author)

def get_booklist_by_id(booklist_id):
    return Booklist.get_by_id(booklist_id)

def get_all_booklists_by_user_id(user_id):
    return Booklist.get_all_by_user_id(user_id)

def update_booklist(booklist_id, title, author):
    Booklist.update(booklist_id, title, author)

def delete_booklist(booklist_id):
    Booklist.delete(booklist_id)
