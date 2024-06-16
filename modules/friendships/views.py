from flask import Blueprint, render_template, request, session, redirect, url_for
from modules.users.models import User
from modules.friendships.models import FriendRequest, Friendship

friendships_bp = Blueprint('friendships', __name__)

@friendships_bp.route('/friends', methods=['GET', 'POST'])
def friends_view():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('users.login'))

    friends = Friendship.get_friends(user_id)
    friend_requests = FriendRequest.get_received_requests(user_id)
    search_result = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'search':
            search_query = request.form.get('search')
            search_result = User.search_user(search_query)
            if search_result:
                search_result.is_friend = Friendship.is_friends(user_id, search_result.id)
        elif action == 'send_request':
            receiver_id = request.form.get('receiver_id')
            if receiver_id:
                FriendRequest.create(user_id, receiver_id)
        elif action == 'accept':
            request_id = request.form.get('request_id')
            FriendRequest.accept_request(request_id)
        elif action == 'reject':
            request_id = request.form.get('request_id')
            FriendRequest.reject_request(request_id)

    return render_template('friends.html', friends=friends, friend_requests=friend_requests, search_result=search_result)
