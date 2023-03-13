import socket
import threading
import json

"""
定义一个客户端类，
    属性：socket、id、name

    行为：
        启动客户端
        帮助信息
        登录
        发送信息
        接收信息
"""


class Client:
    """
    客户端
    """
    prompt = ''
    intro = (
            '[Welcome] 简易聊天室客户端(Cli版)\n' +
            '[Welcome] 输入help来获取帮助\n' +
            '[Help] login nickname - 登录到聊天室，nickname是你选择的昵称\n' +
            '[Help] send message - 发送消息，message是你输入的消息'
    )

    def __init__(self):
        """
        构造
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = None  # 没有登录之前 id 设置为 None
        self.nickname = None  # 昵称设置为 None

    def receive_message_thread(self):
        """
        接受消息线程
        """
        while True:
            # noinspection PyBroadException
            try:
                buffer = self.socket.recv(1024).decode()
                obj = json.loads(buffer)
                # print(obj)
                print('[' + str(obj['sender_nickname']) + '(' + str(obj['sender_id']) + ')' + ']', obj['message'])
            except Exception:
                print('[Client] 无法从服务器获取数据')

    def send_message_thread(self, message):
        """
        发送消息线程
        :param message: 消息内容
        """
        self.socket.send(json.dumps({
            'type': 'broadcast',
            'sender_id': self.id,
            'message': message
        }).encode())

    def do_help(self, arg):
        """
        帮助
        :param arg: 参数
        """
        command = arg.split(' ')[1]
        if command == 'login':
            print('[Help] login nickname - 登录到聊天室，nickname是你选择的昵称')
        elif command == 'send':
            print('[Help] send message - 发送消息，message是你输入的消息')
        else:
            print('[Help] 没有查询到你想要了解的指令')

    def start(self):
        """
        启动客户端
        """
        self.socket.connect(('127.0.0.1', 7799))
        print(self.intro)
        while True:
            action = input("").strip()
            if action.lower().startswith('help'):
                self.do_help(action)
            elif action.lower().startswith('login'):
                self.do_login(action)
            elif action.lower().startswith('send'):
                self.do_send(action)
            else:
                print('[Help] login nickname - 登录到聊天室，nickname是你选择的昵称')
                print('[Help] send message - 发送消息，message是你输入的消息')

    def do_login(self, args):
        """
        登录聊天室
        :param args: 参数
        """
        nickname = args.split()[1]

        # 将昵称发送给服务器，获取用户id
        self.socket.send(json.dumps({
            'type': 'login',
            'nickname': nickname
        }).encode())
        # 尝试接受数据
        # noinspection PyBroadException
        try:
            buffer = self.socket.recv(1024).decode()
            obj = json.loads(buffer)
            if obj['id']:
                self.nickname = nickname
                self.id = obj['id']
                print('[Client] 成功登录到聊天室')

                # 开启子线程用于接受数据
                thread = threading.Thread(target=self.receive_message_thread)
                thread.daemon = True
                thread.start()
            else:
                print('[Client] 无法登录到聊天室')
        except Exception:
            print('[Client] 无法从服务器获取数据')

    def do_send(self, args):
        """
        发送消息
        :param args: 参数
        """
        message = args[5:]
        # 显示自己发送的消息
        print('[' + str(self.nickname) + '(' + str(self.id) + ')' + ']', message)
        # 开启子线程用于发送数据
        thread = threading.Thread(target=self.send_message_thread, args=(message,))
        thread.daemon = True
        thread.start()


if __name__ == '__main__':
    client = Client()
    client.start()
