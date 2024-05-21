# modules/books/models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.session import Base
import datetime

class Book(Base):
    """
    书籍模型
    
    属性:
        id (int): 书籍ID，主键
        title (str): 书籍标题
        author (str): 书籍作者
        published_date (datetime): 书籍出版日期
        isbn (str): 书籍ISBN编号
        user_id (int): 用户ID，外键，表示书籍所有者
    """
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50), nullable=False)
    published_date = Column(DateTime)
    isbn = Column(String(13))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='books')
