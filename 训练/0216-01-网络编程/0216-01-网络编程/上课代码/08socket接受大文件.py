import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(('www.baidu.com', 80))  # http 默认是 80 端口

# http 请求报文
tcp_client_socket.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

# recv_data = tcp_client_socket.recv(1024)
#
# print(recv_data)
# 百度的网页比较大, 一次性接受不全, 所以可以分很多次进行接受

buffer = []  # 用于收集循环接受的数据
while True:
    binary_data = tcp_client_socket.recv(1024)
    if binary_data:
        buffer.append(binary_data)  # 接受的是二进制的数据
    else:
        break

data = b''.join(buffer)
print(data.decode('utf-8').split('\r\n\r\n'))  # 服务器一般使用 utf-8 编码
print(data.decode('utf-8').split('\r\n\r\n'))

tcp_client_socket.close()
