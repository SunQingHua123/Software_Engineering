# application/application.py

from utils.common import hash_password, validate_password
from utils.config import load_config
from utils.logging import setup_logging, get_logger
from database.session import engine, Base

class Application:
    def __init__(self):
        # 加载配置
        self.config = load_config()
        # 设置日志
        setup_logging()
        self.logger = get_logger(__name__)
        self.logger.info("Application initialized.")
        
        # 初始化数据库
        self.init_database()

    def init_database(self):
        # 创建所有未创建的数据库表
        Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app = Application()
