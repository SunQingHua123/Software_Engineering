from flask import session, abort

def get_user_role(user_id):
    # 假设有一个函数可以根据用户ID获取用户角色
    # 这里简化为从session获取
    return session.get('role', None)

def authorized(role):
    """ 检查用户是否具有所需的角色权限 """
    user_role = get_user_role(session.get('user_id'))
    return user_role in role

def create_circle(name, description, creator_id):
    if not authorized(['admin', 'tutor']):  # 只有管理员和导师可以创建圈子
        abort(403)  # 返回403禁止访问错误
    return Circle.create(name, description, creator_id)

def delete_circle(circle_id):
    if not authorized(['admin']):  # 只有管理员可以删除圈子
        abort(403)
    return Circle.delete(circle_id)

def add_member_to_circle(circle_id, user_id):
    if not authorized(['admin', 'tutor']):  # 管理员和导师可以添加成员
        abort(403)
    return Membership.add_member(circle_id, user_id)

def remove_member_from_circle(circle_id, user_id):
    if not authorized(['admin', 'tutor']):  # 管理员和导师可以移除成员
        abort(403)
    return Membership.remove_member(circle_id, user_id)

def create_discussion(circle_id, creator_id, topic, content):
    if not authorized(['admin', 'tutor', 'student']):  # 所有角色都可以创建讨论
        abort(403)
    return Discussion.create(circle_id, creator_id, topic, content)

def delete_discussion(discussion_id):
    if not authorized(['admin', 'tutor']):  # 只有管理员和导师可以删除讨论
        abort(403)
    return Discussion.delete(discussion_id)
