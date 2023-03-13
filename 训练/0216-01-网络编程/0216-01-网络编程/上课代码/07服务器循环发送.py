import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(('127.0.0.1', 7788))
tcp_server_socket.listen(128)

client_socket, client_address = tcp_server_socket.accept()
# 客户端链接成功之后先发送数据
client_socket.send('欢迎光临正心的小卖铺,这里有 瓜子 花生 矿泉水, 请问需要点什么'.encode('gbk'))
price = {
    '瓜子': '4.5 rmb',
    '花生': '4.5 rmb',
    '矿泉水': '2 rmb',
}
while True:
    recv_data = client_socket.recv(1024)
    data = recv_data.decode('gbk')
    # 客户端会有的操作必须提前写好
    if data in price.keys():
        send_data = f'{data} {price[data]} 需求购买请输入: 购买{data}'
        client_socket.send(send_data.encode('gbk'))
    if data == '拜拜':
        break
    if '购买' in data:
        data = data.strip('购买')  # 购买瓜子
        send_data = f'你消费了 {price[data]} 元'
        client_socket.send(send_data.encode('gbk'))

client_socket.close()
tcp_server_socket.close()
