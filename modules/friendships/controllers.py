from flask import Blueprint
from modules.friendships.views import friends_view

friendships_bp = Blueprint('friendships', __name__)

@friendships_bp.route('/friends', methods=['GET', 'POST'])
def friends():
    return friends_view()
