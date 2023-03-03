# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from lxml import etree

if __name__ == '__main__':
    list_1 = ['\t', 5, 'word!']
    str_1 = ''.join(list_1)
