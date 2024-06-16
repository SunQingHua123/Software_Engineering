from flask import Blueprint
from modules.messages.views import chat_view

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/chat/<int:friend_id>', methods=['GET', 'POST'])
def chat(friend_id):
    return chat_view(friend_id)
