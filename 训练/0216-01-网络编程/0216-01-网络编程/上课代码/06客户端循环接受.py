import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(('127.0.0.1', 7788))

# 循环收发数据
while True:
    # 客户端与服务器谁先发送数据
    recv_data = tcp_client_socket.recv(1024)
    data = recv_data.decode('gbk')
    if data == '欢迎下次光临':
        break
    print('服务器发送的数据为:', data)
    send_data = input('请输入需要发送给服务器的数据')
    tcp_client_socket.send(send_data.encode('gbk'))

tcp_client_socket.close()
