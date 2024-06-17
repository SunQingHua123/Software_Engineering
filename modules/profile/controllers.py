import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from modules.profile.models import Profile

def create_profile(user_id, nickname, avatar, contact_info):
    Profile.create(user_id, nickname, avatar, contact_info)

def get_profile_by_user_id(user_id):
    return Profile.get_by_user_id(user_id)

def update_profile(user_id, nickname, avatar, contact_info):
    Profile.update(user_id, nickname, avatar, contact_info)

def delete_profile(user_id):
    Profile.delete(user_id)
