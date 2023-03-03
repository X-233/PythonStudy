# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from Cryptodome.Cipher import AES
from lxml import etree

if __name__ == '__main__':
    key = b'zhanglin06190000'
    data = b'\xe1\xf6\xcfq\xe2=\xa5\xe2\xaaoe\xff\xca\x99\x18\xf5\xb2\x044o;\x8d'
    da = AES.new(key, AES.MODE_CFB, data[-16:])
    de = da.decrypt(data[:-16])
    print(de.decode())
