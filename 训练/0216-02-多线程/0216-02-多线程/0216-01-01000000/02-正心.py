# -*- coding: utf-8 -*-
"""
### 作业2:

将 tcp 文件下载案例中的代码，用面向对象思想进行封装。

1. 服务器（Server）类
    实例属性：
        + 端口、地址、socket

    实例方法：
        - start 启动服务器方法（创建socket、绑定端口、提供服务）
        - handle_recv 处理客户端请求
        - send_file（发送文件方法）

实现两个对象的通信
"""
import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # self.address = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property  # 特性 计算属性
    def address(self):
        return self.host, self.port

    def start(self):
        self.socket.bind(self.address)
        self.socket.listen(124)

        # 目前只能给一个客户提供服务
        server_socket_with_client, client_address = self.socket.accept()
        # 服务器先发送数据给客户端
        self.send_file(server_socket_with_client, client_address)

        # 接受数据
        self.recv_data(server_socket_with_client, client_address)

        # 关闭客户端与服务器的链接
        server_socket_with_client.close()

    def send_file(self, client_socket, client_address):
        # 默认只发送一次
        client_socket.send('欢迎登录服务器'.encode('gbk'))

    def recv_data(self, client_socket, client_address):
        # 接受数据只有一次
        recv_data = client_socket.recv(1024)
        print(f'客户端{client_address} 发送的数据为', recv_data.decode('gbk'))

    def close(self):
        # 关闭服务器的链接
        self.socket.close()


server = Server('127.0.0.1', 7788)
server.start()
