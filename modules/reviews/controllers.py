import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from modules.reviews.models import Review

class ReviewService:
    """
    书评服务类，提供书评管理的各种功能。
    """

    @staticmethod
    def get_all_reviews():
        """
        查看所有书评信息

        返回:
            list[Review]: 书评对象列表
        """
        return Review.get_all_reviews()

    @staticmethod
    def delete_review(review_id):
        """
        删除书评信息

        参数:
            review_id (int): 书评ID
        """
        Review.delete_review(review_id)

    @staticmethod
    def review_statistics():
        """
        书评统计：系统统计每本书的书评数量

        返回:
            list[dict]: 每本书的书评数量统计列表
        """
        return Review.review_statistics()

    @staticmethod
    def recommend_reviews(limit=10):
        """
        书评推荐：查看点赞数较高的书评信息

        参数:
            limit (int): 返回书评的数量限制,默认是10

        返回:
            list[Review]: 点赞数较高的书评对象列表
        """
        return Review.recommend_reviews(limit)
    
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
        return Review.create_review(content, rating, user_id, book_id)
