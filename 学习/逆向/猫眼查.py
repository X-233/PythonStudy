# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from lxml import etree
import hashlib

if __name__ == '__main__':
    url = 'https://www.maoyan.com/films/522013'
    u = 'method=GET&timeStamp=1669013149708&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36&index=7&channelId=40011&sVersion=1'
    f = hashlib.md5('352'.encode('utf-8')).hexdigest()
    print(f)
    # html = requests.get().text
