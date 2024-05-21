# application/services/message_service.py

class MessageService:
    def __init__(self, session):
        self.session = session

    def get_message(self, message_id):
        """获取消息信息"""
        # 实现获取消息信息逻辑
        pass

    def send_message(self, message_data):
        """发送新消息"""
        # 实现发送消息逻辑
        pass
