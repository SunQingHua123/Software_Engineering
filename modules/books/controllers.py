# modules/books/controllers.py
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from modules.books.models import Book

def create_book(title, author, published_date, isbn, user_id):
    """
    创建书籍
    
    参数:
        title (str): 书籍标题
        author (str): 书籍作者
        published_date (str): 书籍出版日期
        isbn (str): 书籍ISBN编号
        user_id (int): 用户ID
    """
    Book.create(title, author, published_date, isbn, user_id)

def get_books():
    """
    获取所有书籍
    
    返回:
        list[Book]: 书籍对象列表
    """
    return Book.get_all()

def get_book_by_id(book_id):
    """
    根据书籍ID获取书籍信息
    
    参数:
        book_id (int): 书籍ID
    
    返回:
        Book: 书籍对象
    """
    return Book.get_by_id(book_id)

def search_books(title):
    """
    根据书籍标题搜索书籍信息
    
    参数:
        title (str): 书籍标题
    
    返回:
        list[Book]: 书籍对象列表
    """
    return Book.search_by_title(title)

def update_book(book_id, title, author, published_date, isbn):
    """
    更新书籍信息
    
    参数:
        book_id (int): 书籍ID
        title (str): 书籍标题
        author (str): 书籍作者
        published_date (str): 书籍出版日期
        isbn (str): 书籍ISBN编号
    """
    Book.update(book_id, title, author, published_date, isbn)

def delete_book(book_id):
    """
    删除书籍信息
    
    参数:
        book_id (int): 书籍ID
    """
    Book.delete(book_id)
