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
    text = b'CZX1L3T542oCpBRemY/ZE/Fvv+PXiT/rZlwXcs1AI1HVchNSPRIu4qVVmUM+glN/Hato51cDxHI//XLksstAnrJN3o1I32E3+V8jHPDbutAhQRzKSGY1NEqlD+yN7pf//d1cWXNO311VqHWQCE1wkR49wBew5M4t9gTN8CQeZok='
    text_1 = base64.b64decode(text)

    print(text_1)
    #加载密钥,使用私钥解密
    pri_key = open('pri_key.bin').read()

    key = RSA.import_key(pri_key)

    # 生产解密对象, 加密时没加盐,默认b'rsa'
    en = PKCS1_v1_5.new(key)
    en_1 = en.decrypt(text_1, b'rsa')
    print(en_1.decode())

    # #编码
    # en_2 = base64.b64encode(en_1)
    # print(en_2)
