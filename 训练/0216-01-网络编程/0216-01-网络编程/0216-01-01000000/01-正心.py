# -*- coding: utf-8 -*-
"""
### 作业1：

运行网络调试工具代码，使用 Python 给网络调试工具发送文字信息，并接受网络调试工具发送过来的数据

+ 打开网络调试工具，选择 `tcp` 服务器并启动
+ 编写 Python 代码给 `tcp` 服务器发送一条信息（hello world ！）
+ 之后等待服务器发送一条信息回来并接受打印，然后断开连接

"""
import socket

s_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_1.connect(('127.0.0.1', 7788))

s_1.send('hello world ！'.encode('gbk'))
data_1 = []
while True:
    data = s_1.recv(1024)
    if data is None:
        break
    data_1.append(data)

s_1.close()
