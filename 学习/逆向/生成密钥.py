# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from Cryptodome.PublicKey import RSA
from lxml import etree

if __name__ == '__main__':
    #生成密钥(位数)
    rsa = RSA.generate(1024)

    #私钥
    print(rsa.export_key())
    The_private_key = rsa.export_key()
    #公钥
    print(rsa.publickey().export_key())
    The_public_key = rsa.publickey().export_key()

    with open('pub_key.bin', 'wb')as f:
        f.write(The_public_key)
    with open('pri_key.bin', 'wb')as f:
        f.write(The_private_key)
