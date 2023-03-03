# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from Cryptodome.PublicKey import RSA
#加密方法
from Crypto.Cipher import PKCS1_v1_5
from lxml import etree
import base64

if __name__ == '__main__':
    text = '张辉'

    #加载密钥,使用公钥进行加密
    pub_key = open('pub_key.bin').read()

    key = RSA.import_key(pub_key)

    #生产加密对象
    en = PKCS1_v1_5.new(key)
    en_1 = en.encrypt(text.encode())
    print(en_1)

    #编码
    en_2 = base64.b64encode(en_1)
    print(en_2)