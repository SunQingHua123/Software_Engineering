# utils/logging.py

import logging
import logging.config

def setup_logging(default_level=logging.INFO):
    """
    设置日志配置
    
    参数:
        default_level (int): 默认日志级别，默认为 logging.INFO
    """
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': 'app.log'
            },
        },
        'loggers': {
            '': {
                'handlers': ['console', 'file'],
                'level': default_level,
                'propagate': True
            }
        }
    }

    logging.config.dictConfig(logging_config)

def get_logger(name: str) -> logging.Logger:
    """
    获取日志记录器
    
    参数:
        name (str): 日志记录器的名称
    
    返回:
        logging.Logger: 日志记录器实例
    """
    return logging.getLogger(name)
