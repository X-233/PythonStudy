# -*- coding: utf-8 -*-
import socket
import threading
import json


class Server:
    """
    服务器类
    """
    def __init__(self):
        """
        构造
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 链接列表
        self.connections = list()
        # 称呼列表
        self.nicknames = list()

    def user_thread(self, user_id):
        """
        用户子线程
        :param user_id: 用户id
        """
        # 获取用户链接
        connection = self.connections[user_id]
        # 获取用户名字
        nickname = self.nicknames[user_id]
        print('[Server] 用户', user_id, nickname, '加入聊天室')
        # 广播一条信息
        self.broadcast(message='用户 ' + str(nickname) + '(' + str(user_id) + ')' + '加入聊天室')

        # 侦听用户发来的信息
        while True:
            try:
                buffer = connection.recv(1024).decode()
                # 解析成json数据
                obj = json.loads(buffer)
                # 如果是广播指令
                if obj['type'] == 'broadcast':
                    self.broadcast(obj['sender_id'], obj['message'])
                else:
                    print('[Server] 无法解析json数据包:', connection.getsockname(), connection.fileno())
            except Exception as e:
                print('[Server] 连接失效:', connection.getsockname(), connection.fileno())
                self.connections[user_id].close()
                self.connections[user_id] = None
                self.nicknames[user_id] = None

    def broadcast(self, user_id=0, message=''):
        """
        广播
        :param user_id: 用户id(0为系统)
        :param message: 广播内容
        """
        for i in range(1, len(self.connections)):
            if user_id != i:
                self.connections[i].send(json.dumps({
                    'sender_id': user_id,
                    'sender_nickname': self.nicknames[user_id],
                    'message': message
                }).encode())

    def start(self):
        """
        启动服务器
        """
        # 绑定端口
        self.socket.bind(('0.0.0.0', 8000))
        # 启用监听
        self.socket.listen(10)
        print('[Server] 服务器正在运行......')

        # 清空连接
        self.connections.clear()
        self.nicknames.clear()
        self.connections.append(None)
        self.nicknames.append('System')

        # 开始侦听
        while True:
            # 接收连接
            connection, address = self.socket.accept()
            print('[Server] 收到一个新连接', connection.getsockname(), connection.fileno())

            # 尝试接受数据
            try:
                buffer = connection.recv(1024).decode()
                # 解析成json数据
                obj = json.loads(buffer)
                # 如果是连接指令，那么则返回一个新的用户编号，接收用户连接
                if obj['type'] == 'login':

                    self.connections.append(connection)
                    self.nicknames.append(obj['nickname'])

                    # 返回json{'id':编号}
                    connection.send(json.dumps({
                        'id': len(self.connections) - 1
                    }).encode())

                    # 开辟一个新的线程
                    # 如果主线程结束，其他线程一起结束
                    thread = threading.Thread(target=self.user_thread, args=(len(self.connections) - 1,))
                    thread.setDaemon(True)
                    thread.start()
                else:
                    print('[Server] 无法解析json数据包:', connection.getsockname(), connection.fileno())
            except Exception as e:
                print(e)
                print('[Server] 无法接受数据:', connection.getsockname(), connection.fileno())


if __name__ == '__main__':
    server = Server()
    server.start()
