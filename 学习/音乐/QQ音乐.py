# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import json
from pprint import pprint

import requests
from lxml import etree
import re

def Header():
    headers = {
        'Cookie': 'pgv_pvid=4619374500; RK=7knNeePRSf; ptcz=01821b5616eb455ddfca915c454a4acaff3b08fa4c00fc62ef54d78fce7fdb25; fqm_pvqid=8b59ac24-0290-48a9-af41-fbf4f4827e11; fqm_sessionid=41a24209-a326-4dcd-9e48-91c39f100454; pgv_info=ssid=s4701823217; ts_uid=5622696588; ts_last=y.qq.com/n/ryqq/toplist/4; ts_refer=i.y.qq.com/',
        'Referer': 'https://i.y.qq.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    return headers

def proxy():
    IP = []

if __name__ == '__main__':
    url = 'https://y.qq.com/n/ryqq/toplist/4'
    headers = Header()
    html = requests.get(url=url, headers=headers)
    re1 = html.text
    text = re.findall('<script>(.*?)</script>', re1, re.S)[-1]
    text = re.findall('.*DATA__ =(.*)', text, re.S)[0]
    text = re.sub('undefined', '0', text)


    json1 = json.loads(text)
    json2 = json1['songInfoList']
    for i in json2:
        print(i['name'])

    # with open('1.json', 'w', encoding='utf-8')as f:
    #     f.write(text)
