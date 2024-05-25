import pymysql

def get_connection():
    """
    获取数据库连接

    返回:
        connection (pymysql.connections.Connection): 数据库连接
    """
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='moyun',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
