import os
import sys
from datetime import datetime

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from database import get_connection

class Review:
    """
    书评模型
    
    属性:
        id (int): 书评ID,主键
        content (str): 书评内容
        rating (int): 书评评分，整数类型，限制在1到5之间
        created_at (datetime): 书评创建时间
        user_id (int): 书评的用户ID
        book_id (int): 所评书籍的ID
    """
    def __init__(self, id, content, rating, created_at, user_id, book_id):
        self.id = id
        self.content = content
        self.rating = rating
        self.created_at = created_at
        self.user_id = user_id
        self.book_id = book_id

    @staticmethod
    def create_review(content, rating, user_id, book_id):
        """
        创建书评

        参数:
            content (str): 书评内容
            rating (int): 书评评分
            user_id (int): 书评的用户ID
            book_id (int): 所评书籍的ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO reviews (content, rating, created_at, user_id, book_id) VALUES (%s, %s, CURRENT_TIMESTAMP, %s, %s)", (content, rating, user_id, book_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_review_by_id(review_id):
        """
        根据书评ID获取书评信息

        参数:
            review_id (int): 书评ID

        返回:
            Review: 书评对象
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM reviews WHERE id = %s", (review_id,))
                result = cursor.fetchone()
                if result:
                    return Review(*result)
                else:
                    return None
        finally:
            connection.close()

    def update_review(self, content, rating):
        """
        更新书评信息

        参数:
            content (str): 书评内容
            rating (int): 书评评分
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE reviews SET content = %s, rating = %s WHERE id = %s", (content, rating, self.id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def delete_review(review_id):
        """
        删除书评信息

        参数:
            review_id (int): 书评ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM reviews WHERE id = %s", (review_id,))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_reviews_by_book(book_id):
        """
        查看指定书籍的书评信息

        参数:
            book_id (int): 书籍ID

        返回:
            list[Review]: 书评对象列表
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM reviews WHERE book_id = %s", (book_id,))
                result = cursor.fetchall()
                return [Review(*row) for row in result]
        finally:
            connection.close()

    @staticmethod
    def review_statistics():
        """
        书评统计：系统统计每本书的书评数量

        返回:
            list[dict]: 每本书的书评数量统计列表
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT book_id, COUNT(*) as review_count
                    FROM reviews
                    GROUP BY book_id
                """)
                result = cursor.fetchall()
                return [{"book_id": row["book_id"], "review_count": row["review_count"]} for row in result]
        finally:
            connection.close()

    @staticmethod
    def recommend_reviews(limit=10):
        """
        书评推荐：查看点赞数较高的书评信息

        参数:
            limit (int): 返回书评的数量限制,默认是10

        返回:
            list[Review]: 点赞数较高的书评对象列表
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM reviews
                    ORDER BY likes DESC
                    LIMIT %s
                """, (limit,))
                result = cursor.fetchall()
                return [Review(*row) for row in result]
        finally:
            connection.close()

    
    @staticmethod
    def get_all_reviews():
        """
        查看所有书评信息
        
        返回:
            list[Review]: 书评对象列表
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM reviews")
                result = cursor.fetchall()
                return [Review(**row) for row in result]
        finally:
            connection.close()

    @staticmethod
    def delete_review(review_id):
        """
        删除书评信息
        
        参数:
            review_id (int): 书评ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM reviews WHERE id = %s", (review_id,))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def review_statistics():
        """
        书评统计：系统统计每本书的书评数量
        
        返回:
            list[dict]: 每本书的书评数量统计列表
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT book_id, COUNT(*) as review_count
                    FROM reviews
                    GROUP BY book_id
                """)
                result = cursor.fetchall()
                return [{"book_id": row["book_id"], "review_count": row["review_count"]} for row in result]
        finally:
            connection.close()

    @staticmethod
    def recommend_reviews(limit=10):
        """
        书评推荐：查看点赞数较高的书评信息
        
        参数:
            limit (int): 返回书评的数量限制,默认是10
        
        返回:
            list[Review]: 点赞数较高的书评对象列表
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM reviews
                    ORDER BY likes DESC
                    LIMIT %s
                """, (limit,))
                result = cursor.fetchall()
                return [Review(**row) for row in result]
        finally:
            connection.close()