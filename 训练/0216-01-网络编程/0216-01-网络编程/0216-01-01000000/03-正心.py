# -*- coding: utf-8 -*-
"""
### 作业3:

2. 客户端（Client）类

    实例属性：
        + 服务器端口、服务器地址、socket

    实例方法：
        + start 启动服务器方法（创建socket、链接服务器）
        + recv_file（发送请求、接收文件方法）
"""
import socket


class Client:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.post = 7788
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.post))

    def recv_file(self):
        data_1 = []
        while True:
            data = self.socket.recv(1024)
            if data is None:
                break

            data_1.append(data)
        return data_1