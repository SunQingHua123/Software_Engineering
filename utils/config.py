# utils/config.py

import configparser
from typing import Dict

def load_config(config_file: str = 'config.ini') -> Dict[str, Dict[str, str]]:
    """
    加载配置文件
    
    参数:
        config_file (str): 配置文件路径，默认为 'config.ini'
    
    返回:
        dict: 包含配置文件内容的字典
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return {section: dict(config.items(section)) for section in config.sections()}
