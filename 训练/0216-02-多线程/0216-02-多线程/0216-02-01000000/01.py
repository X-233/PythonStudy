"""
修改 socket 的代码,使 socket 服务器能够同时给多个客户端提供服务

    接收到客户端的请求之后，在 files 目录下创建一个 `{客户端地址}.txt` 的文件，用于记录客户端发过来的所有信息
    与客户端进行通信的时候
        + 记录客户端发送的数据到 `{客户端地址}.txt` 文件中，
        + 发送 `你已经有xx条信息记录` 给客户端（信息数量可以从文件中读取）

"""
import socket
import threading


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(128)

        # 可以接收到很多个用户的请求
        while True:
            socket_client, socket_client_addr = self.socket.accept()
            t1 = threading.Thread(target= self.handle_recv, args=(socket_client, socket_client_addr))
            t1.start()

    def handle_recv(self, clt_socket, clt_addr):
        """
        :param clt_socket: 客户端的链接
        :param clt_addr: 客户端的地址
        :return:
        """
        while True:
            print('客户度的ip地址信息', clt_addr)
            recv_data = clt_socket.recv(1024)
            print(recv_data.decode('gbk'))
            if recv_data.decode('gbk') != '结束':
                with open(clt_addr[0] + '_' + str(clt_addr[1]) + '.txt', mode='a', encoding='utf-8')as f:
                    f.write(recv_data.decode('gbk') + '\n')
                clt_socket.send('已经接收'.encode())
            else:

                break
        print('连接断开')
        clt_socket.close()

if __name__ == '__main__':
    serve = Server('127.0.0.1', 7788)
    serve.start()
