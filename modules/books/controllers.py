# modules/books/controllers.py

from sqlalchemy.orm import Session
from database.session import get_db
from modules.books.models import Book
from typing import List, Optional
import datetime

def create_book(title: str, author: str, published_date: Optional[datetime.datetime], isbn: Optional[str], user_id: int) -> Book:
    """
    创建新书籍
    
    参数:
        title (str): 书籍标题
        author (str): 书籍作者
        published_date (datetime): 书籍出版日期
        isbn (str): 书籍ISBN编号
        user_id (int): 用户ID，表示书籍所有者
    
    返回:
        Book: 创建成功的书籍对象
    """
    with get_db() as db:
        new_book = Book(title=title, author=author, published_date=published_date, isbn=isbn, user_id=user_id)
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book

def get_books() -> List[Book]:
    """
    获取所有书籍
    
    返回:
        List[Book]: 包含所有书籍对象的列表
    """
    with get_db() as db:
        return db.query(Book).all()

def get_book_by_id(book_id: int) -> Optional[Book]:
    """
    根据ID获取书籍
    
    参数:
        book_id (int): 书籍ID
    
    返回:
        Optional[Book]: 对应ID的书籍对象，若不存在则返回 None
    """
    with get_db() as db:
        return db.query(Book).filter(Book.id == book_id).first()

def search_books(query: str) -> List[Book]:
    """
    搜索书籍
    
    参数:
        query (str): 搜索关键词
    
    返回:
        List[Book]: 包含符合搜索条件的书籍对象的列表
    """
    with get_db() as db:
        return db.query(Book).filter(Book.title.contains(query) | Book.author.contains(query)).all()

def update_book(book_id: int, title: Optional[str], author: Optional[str], published_date: Optional[datetime.datetime], isbn: Optional[str]) -> Optional[Book]:
    """
    更新书籍信息
    
    参数:
        book_id (int): 书籍ID
        title (str): 书籍标题
        author (str): 书籍作者
        published_date (datetime): 书籍出版日期
        isbn (str): 书籍ISBN编号
    
    返回:
        Optional[Book]: 更新后的书籍对象，若书籍不存在则返回 None
    """
    with get_db() as db:
        book = db.query(Book).filter(Book.id == book_id).first()
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if published_date:
                book.published_date = published_date
            if isbn:
                book.isbn = isbn
            db.commit()
            db.refresh(book)
            return book
        else:
            return None

def delete_book(book_id: int) -> bool:
    """
    删除书籍
    
    参数:
        book_id (int): 书籍ID
    
    返回:
        bool: 删除成功返回 True，否则返回 False
    """
    with get_db() as db:
        book = db.query(Book).filter(Book.id == book_id).first()
        if book:
            db.delete(book)
            db.commit()
            return True
        else:
            return False
