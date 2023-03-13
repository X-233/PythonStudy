# -*- coding: utf-8 -*-
"""
### 作业1：

运行网络调试工具代码，使用 Python 给网络调试工具发送文字信息，并接受网络调试工具发送过来的数据

+ 打开网络调试工具，选择 `tcp` 服务器并启动
+ 编写 Python 代码给 `tcp` 服务器发送一条信息（hello world ！）
+ 之后等待服务器发送一条信息回来并接受打印，然后断开连接

"""
import socket

# tcp_socket_client  变量名 对象 socket 链接
tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket_client.connect(('127.0.0.1', 7788))

# 客户端的链接对象
tcp_socket_client.send('hello world ！'.encode('utf-8'))

recv_data = tcp_socket_client.recv(1024)
print('服务器发送回来的数据:', recv_data.decode('utf-8'))

tcp_socket_client.close()
