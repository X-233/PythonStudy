# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from lxml import etree
import binascii
import base64
import hashlib

if __name__ == '__main__':
    hello = 'hello 世界'
    e = hello.encode('utf-8')
    print(e)
    b = binascii.b2a_hex(e)

    print(b)

    # base64编码
    v = '比好'
    print(base64.b64encode(v.encode('utf-8')))

    # 解码
    c = '5q+U5aW9'
    print(base64.b64decode(c.encode('utf-8')).decode('utf-8'))

    # md5
    pas = '1234'
    md5 = hashlib.md5()

    md5.update(pas.encode())
    # 小写变大写
    print(md5.hexdigest().upper())