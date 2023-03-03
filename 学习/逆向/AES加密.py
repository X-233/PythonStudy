# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from Cryptodome.Cipher import AES
from Cryptodome import Random
from lxml import etree

if __name__ == '__main__':
    # 加密参数16位数, 24位数, 32位数
    key = b'zhanglin06190000'

    #密钥,随机密钥,iv混淆加盐
    iv = Random.new().read(AES.block_size)
    print(iv)
    #创建aes对象(密钥, 模式, 加盐)
    aes = AES.new(key, AES.MODE_CFB, iv)

    data = '张辉'
    en = aes.encrypt(data.encode())
    print(en + iv)
