import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from database import get_connection

class Log:
    def __init__(self, id, user_id, title, content, created_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.created_at = created_at

    @staticmethod
    def create(user_id, title, content):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO logs (user_id, title, content)
                    VALUES (%s, %s, %s)
                """, (user_id, title, content))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_by_id(log_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM logs WHERE id = %s", (log_id,))
                result = cursor.fetchone()
                return Log(**result) if result else None
        finally:
            connection.close()

    @staticmethod
    def get_all_by_user_id(user_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM logs WHERE user_id = %s", (user_id,))
                result = cursor.fetchall()
                return [Log(**row) for row in result]
        finally:
            connection.close()

    @staticmethod
    def update(log_id, title, content):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE logs
                    SET title = %s, content = %s
                    WHERE id = %s
                """, (title, content, log_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def delete(log_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM logs WHERE id = %s", (log_id,))
            connection.commit()
        finally:
            connection.close()
