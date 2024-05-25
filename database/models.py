from database import get_connection

def create_tables():
    """
    创建数据库表
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # 创建用户表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(80) NOT NULL UNIQUE,
                    password VARCHAR(200) NOT NULL,
                    role VARCHAR(20) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            # 创建书籍表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(200) NOT NULL,
                    author VARCHAR(100) NOT NULL,
                    published_date DATE,
                    isbn VARCHAR(13)
                )
            """)
            # 创建书评表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reviews (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    content TEXT NOT NULL,
                    rating INT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    user_id INT NOT NULL,
                    book_id INT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (book_id) REFERENCES books(id)
                )
            """)
            # 创建圈子表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS circles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    user_id INT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            # 创建消息表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    content TEXT NOT NULL,
                    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    sender_id INT NOT NULL,
                    receiver_id INT NOT NULL,
                    FOREIGN KEY (sender_id) REFERENCES users(id),
                    FOREIGN KEY (receiver_id) REFERENCES users(id)
                )
            """)
            # 创建好友关系表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS friendships (
                    user_id INT NOT NULL,
                    friend_id INT NOT NULL,
                    PRIMARY KEY (user_id, friend_id),
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (friend_id) REFERENCES users(id)
                )
            """)
        connection.commit()
    finally:
        connection.close()
