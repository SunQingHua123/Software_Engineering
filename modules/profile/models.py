import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from database import get_connection

class Profile:
    def __init__(self, user_id, nickname, avatar, contact_info):
        self.user_id = user_id
        self.nickname = nickname
        self.avatar = avatar
        self.contact_info = contact_info

    @staticmethod
    def create(user_id, nickname, avatar, contact_info):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO profiles (user_id, nickname, avatar, contact_info)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, nickname, avatar, contact_info))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_by_user_id(user_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM profiles WHERE user_id = %s", (user_id,))
                result = cursor.fetchone()
                return Profile(**result) if result else None
        finally:
            connection.close()

    @staticmethod
    def update(user_id, nickname, avatar, contact_info):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE profiles
                    SET nickname = %s, avatar = %s, contact_info = %s
                    WHERE user_id = %s
                """, (nickname, avatar, contact_info, user_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def delete(user_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM profiles WHERE user_id = %s", (user_id,))
            connection.commit()
        finally:
            connection.close()
