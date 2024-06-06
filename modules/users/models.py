import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from database import get_connection

class User:
    def __init__(self, id, username, email, password, role, created_at):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.created_at = created_at

    @staticmethod
    def create(username, email, password, role):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO users (username, email, password, role)
                    VALUES (%s, %s, %s, %s)
                """, (username, email, password, role))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_by_id(user_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
                result = cursor.fetchone()
                return User(**result) if result else None
        finally:
            connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                result = cursor.fetchall()
                return [User(**row) for row in result]
        finally:
            connection.close()

    @staticmethod
    def update(user_id, username, email, password, role):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE users
                    SET username = %s, email = %s, password = %s, role = %s
                    WHERE id = %s
                """, (username, email, password, role, user_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def delete(user_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            connection.commit()
        finally:
            connection.close()
