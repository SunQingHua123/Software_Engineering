from datetime import datetime
from database import get_connection
from modules.users.models import User

class FriendRequest:
    def __init__(self, id, sender_id, receiver_id, status, created_at):
        self.id = id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.status = status
        self.created_at = created_at
        self.sender = User.get_by_id(sender_id)
        self.receiver = User.get_by_id(receiver_id)

    @staticmethod
    def create(sender_id, receiver_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO friend_requests (sender_id, receiver_id, status, created_at)
                    VALUES (%s, %s, 'pending', %s)
                """, (sender_id, receiver_id, datetime.now()))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_received_requests(user_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM friend_requests
                    WHERE receiver_id = %s AND status = 'pending'
                """, (user_id,))
                result = cursor.fetchall()
                return [FriendRequest(**row) for row in result]
        finally:
            connection.close()

    @staticmethod
    def accept_request(request_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE friend_requests SET status = 'accepted' WHERE id = %s", (request_id,))
                cursor.execute("SELECT sender_id, receiver_id FROM friend_requests WHERE id = %s", (request_id,))
                result = cursor.fetchone()
                if result:
                    Friendship.create(result['sender_id'], result['receiver_id'])
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def reject_request(request_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE friend_requests SET status = 'rejected' WHERE id = %s", (request_id,))
            connection.commit()
        finally:
            connection.close()

class Friendship:
    def __init__(self, user_id, friend_id):
        self.user_id = user_id
        self.friend_id = friend_id

    @staticmethod
    def create(user_id, friend_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO friendships (user_id, friend_id)
                    VALUES (%s, %s), (%s, %s)
                """, (user_id, friend_id, friend_id, user_id))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_friends(user_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT users.* FROM users
                    JOIN friendships ON users.id = friendships.friend_id
                    WHERE friendships.user_id = %s
                """, (user_id,))
                result = cursor.fetchall()
                return [User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    password=row['password'],
                    role=row['role'],
                    created_at=row['created_at']
                ) for row in result]
        finally:
            connection.close()

    @staticmethod
    def is_friends(user_id, friend_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM friendships
                    WHERE (user_id = %s AND friend_id = %s) OR (user_id = %s AND friend_id = %s)
                """, (user_id, friend_id, friend_id, user_id))
                result = cursor.fetchone()
                return result is not None
        finally:
            connection.close()
