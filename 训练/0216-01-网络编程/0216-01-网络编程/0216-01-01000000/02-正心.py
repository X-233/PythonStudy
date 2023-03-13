# -*- coding: utf-8 -*-
"""
### 作业2:

将tcp文件下载案例中的代码，用面向对象思想进行封装。

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
    def __init__(self):
        self.ip = '127.0.0.1'
        self.post = 7788
        self.socket = Server.start(self)

    def start(self):
        s_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_1.bind((self.ip, self.post))
        s_1.listen(128)
        client_socket, client_address = s_1.accept()
        return [client_socket, client_address]

    def handle_recv(self):
        self.socket[0].send('已经连接上服务端'.encode('gbk'))
        client_data = self.socket[0].recv(1024)
        print(client_data)

    def send_file(self):
        self.socket[0].sendfile(file='.课程资料\\课前注意.md')

if __name__ == '__main__':
    S_1 = Server()

    S_1.start()
    S_1.send_file()