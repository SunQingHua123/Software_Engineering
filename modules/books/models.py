import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from database import get_connection

class Book:
    """
    书籍模型
    
    属性:
        id (int): 书籍ID，主键
        title (str): 书籍标题
        author (str): 书籍作者
        published_date (datetime): 书籍出版日期
        isbn (str): 书籍ISBN编号
    """
    def __init__(self, id, title, author, published_date, isbn):
        self.id = id
        self.title = title
        self.author = author
        self.published_date = published_date
        self.isbn = isbn

    @staticmethod
    def create(title, author, published_date, isbn):
        """
        创建书籍
        
        参数:
            title (str): 书籍标题
            author (str): 书籍作者
            published_date (str): 书籍出版日期
            isbn (str): 书籍ISBN编号
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO books (title, author, published_date, isbn)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (title, author, published_date, isbn))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_all(sort=None):
        """
        获取所有书籍
        
        返回:
            list[Book]: 书籍对象列表
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books"
                if sort:
                    sql += f" ORDER BY {sort}"
                cursor.execute(sql)
                result = cursor.fetchall()
                return [Book(**row) for row in result]
        finally:
            connection.close()

    @staticmethod
    def get_by_id(book_id):
        """
        根据书籍ID获取书籍信息
        
        参数:
            book_id (int): 书籍ID
        
        返回:
            Book: 书籍对象
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
                result = cursor.fetchone()
                return Book(**result) if result else None
        finally:
            connection.close()

    @staticmethod
    def search_by_title(title, sort=None):
        """
        根据书籍标题搜索书籍信息
        
        参数:
            title (str): 书籍标题
            sort(str):是否对某属性进行排序
        
        返回:
            list[Book]: 书籍对象列表
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE title LIKE %s"
                if sort:
                    sql += f" ORDER BY {sort}"
                cursor.execute(sql, ('%' + title + '%',))
                result = cursor.fetchall()
                return [Book(**row) for row in result]
        finally:
            connection.close()

    @staticmethod
    def update(book_id, title, author, published_date, isbn):
        """
        更新书籍信息
        
        参数:
            book_id (int): 书籍ID
            title (str): 书籍标题
            author (str): 书籍作者
            published_date (str): 书籍出版日期
            isbn (str): 书籍ISBN编号
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE books
                    SET title = %s, author = %s, published_date = %s, isbn = %s
                    WHERE id = %s
                """
                cursor.execute(sql, (title, author, published_date, isbn, book_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def delete(book_id):
        """
        删除书籍信息
        
        参数:
            book_id (int): 书籍ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
            connection.commit()
        finally:
            connection.close()
