from flask import Blueprint, render_template, session, redirect, url_for, request
from modules.messages.models import Message
from modules.users.models import User

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/chat/<int:friend_id>', methods=['GET', 'POST'])
def chat_view(friend_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('users.login'))

    friend = User.get_by_id(friend_id)
    if not friend:
        return redirect(url_for('messages.messages'))

    if request.method == 'POST':
        content = request.form.get('message')
        Message.create(sender_id=user_id, receiver_id=friend_id, content=content)

    messages = Message.get_conversation(user_id, friend_id)

    return render_template('chat.html', friend=friend, user_id = user_id, messages=messages)
