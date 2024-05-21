# database/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+pymysql://root:password@localhost/mydatabase"

# 创建数据库引擎
engine = create_engine(DATABASE_URL, echo=True)

# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基类
Base = declarative_base()

def get_db():
    """
    获取数据库会话
    
    返回:
        session: 数据库会话
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
