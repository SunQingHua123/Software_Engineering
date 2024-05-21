# database/models.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    """
    用户模型
    
    属性:
        id (int): 用户ID，主键
        username (str): 用户名，唯一
        email (str): 用户邮箱，唯一
        password_hash (str): 用户密码哈希
        created_at (datetime): 用户创建时间
    """
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Book(Base):
    """
    书籍模型
    
    属性:
        id (int): 书籍ID，主键
        title (str): 书籍标题
        author (str): 书籍作者
        published_date (datetime): 书籍出版日期
        isbn (str): 书籍ISBN编号
        user_id (int): 用户ID，外键
    """
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50), nullable=False)
    published_date = Column(DateTime)
    isbn = Column(String(13))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='books')

User.books = relationship('Book', order_by=Book.id, back_populates='user')
