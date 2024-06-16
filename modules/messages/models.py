from database import get_connection

# Message class
class Message:
    def __init__(self, id, sender_id, receiver_id, content, timestamp):
        self.id = id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = timestamp

    @staticmethod
    def create(sender_id, receiver_id, content):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO messages (sender_id, receiver_id, content, timestamp)
                    VALUES (%s, %s, %s, NOW())
                """, (sender_id, receiver_id, content))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_conversation(user_id, friend_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM messages
                    WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s)
                    ORDER BY timestamp
                """, (user_id, friend_id, friend_id, user_id))
                result = cursor.fetchall()
                return [Message(**row) for row in result]
        finally:
            connection.close()

