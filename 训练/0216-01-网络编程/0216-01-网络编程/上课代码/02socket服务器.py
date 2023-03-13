import socket

# 1. 创建 socket 对
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定本地信息
address = ('127.0.0.1', 7788)
tcp_server_socket.bind(address)

# 3. 等待客户端的链接
tcp_server_socket.listen(128)  # 设置同时监听的数据

print('服务器已经启动了,等待客户端的链接')
# 4. 等待客户上门, 就会产生一个新的链接对象
# client_socket 服务器与客户端的链接
# client_address 客户端的地址
client_socket, client_address = tcp_server_socket.accept()
# 循环监听客户端的链接需要丢到 while 多线程解决并发问题 下节课

# 5.1 服务器发送数据给客户端
client_socket.send('尊贵的客户 请问需要什么样的服务'.encode('gbk'))
print('客户端的信息:', client_address)
# 5.2 服务器接受客户端的信息
recv_data = client_socket.recv(1024)
print('接收到客户端的数据:', recv_data.decode('gbk'))

# 6. 结束
# 结束与客户端的链接
client_socket.close()
# 关闭服务器
tcp_server_socket.close()

# 服务器可以用 input 进行手动收入吗 ?

# 代码逻辑层面没有问题
# 实际做业务需求是不行的
