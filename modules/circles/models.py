import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from database import get_connection

class Circle:
    def __init__(self, circle_id, name, description, creator_id):
        """
        初始化圈子对象
        :param circle_id: 圈子ID
        :param name: 圈子名称
        :param description: 圈子描述
        :param creator_id: 创建者ID（管理员或导师）
        """
        self.circle_id = circle_id
        self.name = name
        self.description = description
        self.creator_id = creator_id

    @staticmethod
    def create(name, description, creator_id):
        """
        创建新的圈子
        :param name: 圈子名称
        :param description: 圈子描述
        :param creator_id: 创建者ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO circles (name, description, creator_id)
                    VALUES (%s, %s, %s)
                """, (name, description, creator_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_by_id(circle_id):
        """
        根据圈子ID获取圈子信息
        :param circle_id: 圈子ID
        :return: Circle对象
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM circles WHERE circle_id = %s", (circle_id,))
                result = cursor.fetchone()
                return Circle(**result) if result else None
        finally:
            connection.close()

    @staticmethod
    def update(circle_id, name, description):
        """
        更新圈子信息
        :param circle_id: 圈子ID
        :param name: 更新后的圈子名称
        :param description: 更新后的圈子描述
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE circles
                    SET name = %s, description = %s
                    WHERE circle_id = %s
                """, (name, description, circle_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def delete(circle_id):
        """
        删除圈子
        :param circle_id: 圈子ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM circles WHERE circle_id = %s", (circle_id,))
            connection.commit()
        finally:
            connection.close()

class Discussion:
    def __init__(self, discussion_id, circle_id, creator_id, topic, content):
        """
        初始化讨论对象
        :param discussion_id: 讨论ID
        :param circle_id: 所属圈子ID
        :param creator_id: 讨论创建者ID
        :param topic: 讨论主题
        :param content: 讨论内容
        """
        self.discussion_id = discussion_id
        self.circle_id = circle_id
        self.creator_id = creator_id
        self.topic = topic
        self.content = content

    @staticmethod
    def create(circle_id, creator_id, topic, content):
        """
        创建新的讨论
        :param circle_id: 所属圈子ID
        :param creator_id: 创建者ID
        :param topic: 讨论主题
        :param content: 讨论内容
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO discussions (circle_id, creator_id, topic, content)
                    VALUES (%s, %s, %s, %s)
                """, (circle_id, creator_id, topic, content))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def delete(discussion_id):
        """
        删除讨论
        :param discussion_id: 讨论ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM discussions WHERE discussion_id = %s", (discussion_id,))
            connection.commit()
        finally:
            connection.close()

class Membership:
    def __init__(self, membership_id, circle_id, user_id):
        """
        初始化成员关系对象
        :param membership_id: 成员关系ID
        :param circle_id: 圈子ID
        :param user_id: 用户ID
        """
        self.membership_id = membership_id
        self.circle_id = circle_id
        self.user_id = user_id

    @staticmethod
    def add_member(circle_id, user_id):
        """
        添加成员到圈子
        :param circle_id: 圈子ID
        :param user_id: 用户ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO memberships (circle_id, user_id)
                    VALUES (%s, %s)
                """, (circle_id, user_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def remove_member(circle_id, user_id):
        """
        从圈子中移除成员
        :param circle_id: 圈子ID
        :param user_id: 用户ID
        """
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM memberships WHERE circle_id = %s AND user_id = %s", (circle_id, user_id))
            connection.commit()
        finally:
            connection.close()
