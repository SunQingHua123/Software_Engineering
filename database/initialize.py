# database/initialize.py

import pymysql

def initialize_database():
    """
    初始化数据库
    """
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # 创建数据库
            sql_create_database = "CREATE DATABASE IF NOT EXISTS moyun"
            cursor.execute(sql_create_database)

            # 使用数据库
            sql_use_database = "USE moyun"
            cursor.execute(sql_use_database)

            # 创建书籍表
            sql_create_books = """
                CREATE TABLE IF NOT EXISTS books (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(100) NOT NULL,
                    author VARCHAR(50) NOT NULL,
                    published_date DATE,
                    isbn VARCHAR(13),
                    user_id INT
                )
            """
            cursor.execute(sql_create_books)

            # 创建用户表
            sql_create_users = """
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    password VARCHAR(100) NOT NULL
                )
            """
            cursor.execute(sql_create_users)

            connection.commit()
    finally:
        connection.close()

if __name__ == "__main__":
    initialize_database()
