import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from database import get_connection

class Booklist:
    def __init__(self, id, user_id, title, author, created_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.author = author
        self.created_at = created_at

    @staticmethod
    def create(user_id, title, author):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO booklists (user_id, title, author)
                    VALUES (%s, %s, %s)
                """, (user_id, title, author))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_by_id(booklist_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM booklists WHERE id = %s", (booklist_id,))
                result = cursor.fetchone()
                return Booklist(**result) if result else None
        finally:
            connection.close()

    @staticmethod
    def get_all_by_user_id(user_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM booklists WHERE user_id = %s", (user_id,))
                result = cursor.fetchall()
                return [Booklist(**row) for row in result]
        finally:
            connection.close()

    @staticmethod
    def update(booklist_id, title, author):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE booklists
                    SET title = %s, author = %s
                    WHERE id = %s
                """, (title, author, booklist_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def delete(booklist_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM booklists WHERE id = %s", (booklist_id,))
            connection.commit()
        finally:
            connection.close()
