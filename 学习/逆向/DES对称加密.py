# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from Cryptodome.Cipher import DES
from lxml import etree

def zhe(text):
# 将text变成8的整数倍
    while len(text) % 8 != 0:
        text += ' '
    return text
if __name__ == '__main__':

    # key密钥,八位
    key = b'23142312'

    #得到加密对象
    des = DES.new(key=key, mode=DES.MODE_ECB)

    #对数据进行加密, 数据长度必须是8的整数倍

    word = 'fsfafasfdasdf'
    word = zhe(word)

    encrypt = des.encrypt(word.encode())
    print(encrypt)

    de = des.decrypt(encrypt).decode().strip()

    print(de)
