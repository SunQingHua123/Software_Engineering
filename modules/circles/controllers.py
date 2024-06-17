from database import get_connection

def create_circle(name, description, user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO circles (name, description, user_id) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, description, user_id))
            connection.commit()
            return cursor.lastrowid  # 返回新创建的圈子ID
    finally:
        connection.close()

def get_circles():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM circles"
            cursor.execute(sql)
            return cursor.fetchall()  # 返回所有圈子的列表
    finally:
        connection.close()

def delete_circle(circle_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM circles WHERE id = %s"
            cursor.execute(sql, (circle_id,))
            connection.commit()
            return cursor.rowcount > 0  # 返回删除是否成功
    finally:
        connection.close()

def add_member_to_circle(circle_id, user_id, role='member'):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO circle_members (circle_id, user_id, role) VALUES (%s, %s, %s)"
            cursor.execute(sql, (circle_id, user_id, role))
            connection.commit()
            return True
    finally:
        connection.close()

def remove_member_from_circle(circle_id, user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM circle_members WHERE circle_id = %s AND user_id = %s"
            cursor.execute(sql, (circle_id, user_id))
            connection.commit()
            return True
    finally:
        connection.close()

def get_circle_by_id(circle_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM circles WHERE id = %s"
            cursor.execute(sql, (circle_id,))
            return cursor.fetchone()  # 返回查询到的圈子信息
    finally:
        connection.close()

def update_circle(circle_id, name, description):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE circles SET name = %s, description = %s WHERE id = %s"
            cursor.execute(sql, (name, description, circle_id))
            connection.commit()
            return True
    finally:
        connection.close()
def create_discussion(circle_id, creator_id, topic, content):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO discussions (circle_id, creator_id, topic, content) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (circle_id, creator_id, topic, content))
            connection.commit()
            return cursor.lastrowid  # 返回新创建的讨论ID
    finally:
        connection.close()

def delete_discussion(discussion_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM discussions WHERE id = %s"
            cursor.execute(sql, (discussion_id,))
            connection.commit()
            return cursor.rowcount > 0  # 返回删除是否成功
    finally:
        connection.close()

def get_discussion_by_id(discussion_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM discussions WHERE id = %s"
            cursor.execute(sql, (discussion_id,))
            return cursor.fetchone()  # 返回查询到的讨论信息
    finally:
        connection.close()

