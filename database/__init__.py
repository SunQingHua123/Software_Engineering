# database/__init__.py
from .initialize import initialize_database

# 在模块被导入时自动执行数据库初始化
initialize_database()