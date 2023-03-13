import socket

# 1. 创建 socket 对象
# socket.AF_INET  ipv4 的版本
# socket.SOCK_STREAM tcp协议
tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 目的信息
server_ip = '127.0.0.1'
server_port = 7788

# 3. 链接服务器
tcp_socket_client.connect((server_ip, server_port))

message = 'hello world !'

# 4.1 发送数据给服务器
tcp_socket_client.send(message.encode('gbk'))

# 4.2 接受服务器返回的数据
recv_data = tcp_socket_client.recv(1024)  # bit
print('recv_data:', recv_data)
print('recv_data:', recv_data.decode('gbk'))  # 接受服务器的数据必须解码

# 大文件需要循环接受

# 5. 关闭与服务器的链接
tcp_socket_client.close()

# socket -> urllib --> requests
