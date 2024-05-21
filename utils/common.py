# utils/common.py

import hashlib

def hash_password(password: str) -> str:
    """
    生成密码的哈希值
    
    参数:
        password (str): 原始密码字符串
    
    返回:
        str: 哈希后的密码字符串
    """
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(password: str, hashed: str) -> bool:
    """
    验证密码与其哈希值是否匹配
    
    参数:
        password (str): 原始密码字符串
        hashed (str): 哈希后的密码字符串
    
    返回:
        bool: 如果匹配返回 True，否则返回 False
    """
    return hash_password(password) == hashed
