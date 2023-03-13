import threading
import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def address(self):
        return self.host, self.port

    def start(self):
        self.socket.bind(self.address)
        self.socket.listen(124)  # 参考值
        """
            当客户端链接成功之后,专门开启一条线程进行收发数据的操作
        """
        # 循环等待客户端的链接, 可能会有很多个客户上门
        while True:
            server_socket_with_client, client_address = self.socket.accept()
            # 接收到客户之后, 专门处理收发数据
            # self.send_file(server_socket_with_client, client_address)
            # self.recv_data(server_socket_with_client, client_address)
            # server_socket_with_client.close()
            # self.handler_connection_client(server_socket_with_client, client_address)
            # 客户上门之后专门开一条新的线程进行处理, 不阻塞后续的操作
            t1 = threading.Thread(target=self.handler_connection_client,
                                  args=(server_socket_with_client, client_address))
            t1.start()

    def handler_connection_client(self, client_socket, client_address):
        while True:
            self.send_file(client_socket, client_address)
            ret = self.recv_data(client_socket, client_address)
            if ret:
                break
        client_socket.close()  # 关闭与客户端的链接
        # 线程对象里面没有逻辑可以执行的时候,会自动销毁  --> 垃圾回收机制

    def send_file(self, client_socket, client_address):
        # 服务器发送给客户端的逻辑需要提前好
        client_socket.send('欢迎登录服务器'.encode('gbk'))

    def recv_data(self, client_socket, client_address):
        recv_data = client_socket.recv(1024)
        data = recv_data.decode('gbk')
        if data == '拜拜':  # 如果客户端发送 拜拜 就结束链接
            return True
        print(f'客户端{client_address} 发送的数据为', recv_data.decode('gbk'))
        return None

    def close(self):
        self.socket.close()


server = Server('127.0.0.1', 7788)
server.start()
