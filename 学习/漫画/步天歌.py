# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰

import requests
import redis
from random import choice as ch
from lxml import etree
from time import sleep
import os
# from urllib3 import request as req
from concurrent.futures import ThreadPoolExecutor
import random


path_3 = os.getcwd() + '\\漫画大全'
word = input('要爬取漫画的网址: \n')
# word = 'https://cn.godamanga.com/manga/butiange-xiada/'
def Analysy(H, IP):
    # temp = 'X_CACHE_KEY=05e0d888c9e4200d2beaa4fd0e2261cf; wpmanga-reading-history=W3siaWQiOjQ5Njk4LCJjIjoiMTE3OTA4NiIsInAiOjEsImkiOiIiLCJ0IjoxNjY0NDg2MjYzfSx7ImlkIjo0NjEyNCwiYyI6IjEzMzgwNjMiLCJwIjoxLCJpIjoiIiwidCI6MTY2NTMyMjc4OX0seyJpZCI6MzAzOTgsImMiOiIxMzI1MDQ4IiwicCI6MSwiaSI6IiIsInQiOjE2NjUzNjI3MzB9LHsiaWQiOjQ5MDcyLCJjIjoiMTE4MTcyMSIsInAiOjEsImkiOiIiLCJ0IjoxNjY1MzcwNTQxfSx7ImlkIjoyNjc2OCwiYyI6IjEyMDYxNzgiLCJwIjoxLCJpIjoiIiwidCI6MTY2NTM5OTk4MX1d'
    #
    # cookie = {i.split('=')[0]: i.split('=')[-1] for i in temp.split('; ')}
    # print(str(IP1))
    m = True
    while m:
        H1 = ch(H)
        IP1 = ch(IP)
        try:
            response = requests.get(url=word, headers=H1, timeout=None) #verify=False
            print(response.status_code)
            response.encoding = 'UTF-8'
            m = False
        except requests.exceptions.ConnectionError as r:
            r.status_code = "Connection refused"
            # socket.setdefaulttimeout(500)
            sleep(random.random()*4)
            print(r)
            continue
    return response
    # print(re2)

def Analysy_1(response):
    # 章节
    xpath = etree.HTML(response.text)
    response.close()
    re3 = xpath.xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/ul/li')
    # 漫画名称
    title = (xpath.xpath('/html/head/title/text()')[0]).strip()
    title = str(title).split('-')[0].strip()
    print(title)
    name_urls = {}
    for i in re3:
        name_urls.update({i.xpath('./a/@href')[0]: str(i.xpath('./a/text()')[0]).strip().replace(' ', '_').replace('?', '').replace('!', '')})

    keys = list(name_urls.keys())
    values = list(name_urls.values())
    keys.reverse()
    values.reverse()
    name_urls = dict(zip(keys, values))

    for key, value in name_urls.items():
        print(key + '   ' + value)
    return name_urls, title

def Analysis():
    r4 = redis.StrictRedis(host="180.76.187.206",
                           port=6379,
                           password="zhanglin",
                           db=4,
                           username="default")
    IP = r4.smembers('IP_3')
    # IP = r4.lrange('IP_2', 0 , -1)
    Ips = []
    Header = r4.lrange('Headers', 0, -1)
    Headers = []
    r4.close()

    for i in Header:
        #编码, byte类型转换
        i = i.decode('utf-8')
        Headers.append({'User-Agent': i})

    H = []
    for i in Header:
        #编码, byte类型转换
        i = i.decode('utf-8')
        H.append(i)

    m = {
        'referer': 'https://cn.godamanga.com/',
        'cookie': 'X_CACHE_KEY=05e0d888c9e4200d2beaa4fd0e2261cf; wpmanga-reading-history=W3siaWQiOjQ5Njk4LCJjIjoiMTE3OTA4NiIsInAiOjEsImkiOiIiLCJ0IjoxNjY0NDg2MjYzfSx7ImlkIjo0NjEyNCwiYyI6IjEzMzgwNjMiLCJwIjoxLCJpIjoiIiwidCI6MTY2NTMyMjc4OX0seyJpZCI6MzAzOTgsImMiOiIxMzI1MDQ4IiwicCI6MSwiaSI6IiIsInQiOjE2NjUzNjI3MzB9LHsiaWQiOjQ5MDcyLCJjIjoiMTE4MTcyMSIsInAiOjEsImkiOiIiLCJ0IjoxNjY1MzcwNTQxfSx7ImlkIjoyNjc2OCwiYyI6IjEzMzY2MTEiLCJwIjoxLCJpIjoiIiwidCI6MTY2NTQwNzYwMH0seyJpZCI6NDcwNDAsImMiOiIxMzM5NTM1IiwicCI6MSwiaSI6IiIsInQiOjE2NjU0MDc5NzN9LHsiaWQiOjE4NjU2NjIsImMiOiIxMzQxMjM4IiwicCI6MSwiaSI6IiIsInQiOjE2NjU0MTcxNDV9XQ%3D%3D',

        }
    for i in Headers:
        i.update(m)

    for i in IP:
        i = i.decode('utf-8')
        # if 'https' in i:
        #     Ips.append({'HTTPS': i})
        # else:
        #     Ips.append({'HTTP': i})
        # Ips.append(i)
        Ips.append({'http': 'http://' + i})
    proxy = [{'HTTPS': 'https://165.225.210.85:10605'},
             {'HTTPS': 'https://20.206.106.192:8123'},
             {'HTTPS': 'https://169.57.1.85:8123'},
             {'HTTPS': 'https://20.24.43.214:8123'},
             {'HTTPS': 'https://5.178.245.20:8080'},
             {'HTTPS': 'https://49.0.2.242:8090'},
             ]

    return Headers, Ips, H

def Down_img(IP, H_2, i, s_title, title, i_1):
    # 设置代理
    # proxy = req.ProxyHandler(IP)
    # r = req.build_opener(proxy)
    # # 设置请求头
    # r.addheaders = [('User-Agent', H_2)]
    # req.install_opener(r)
    # read = req.urlopen(i, timeout=30)
    m = True
    while m:
        try:
            response = requests.get(url=i, timeout=25)  # verify=False
            m = False
            with open(path_3 + f'\\漫画\\{title}\\{s_title}\\{i_1}', 'wb') as f:
                f.write(response.content)
                f.flush()
                f.close()
            response.close()
        except requests.exceptions.ConnectionError as r:
            r.status_code = "Connection refused"
            # socket.setdefaulttimeout(500)
            sleep(random.random() * 4)
            print(r)
            continue

def Save_image(url, s_title, title, H, IP, H_2):
    m = True
    while m:
        H1 = ch(H)
        H1['referer'] = word
        try:
            re1 = requests.get(url=url, timeout=None)
            m = False
        except Exception as e:
            print(e)
            sleep(3)
            continue
    Html = re1.text
    xpath = etree.HTML(Html)
    imgs = []

    img = xpath.xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[1]//img')

    for i in img:
        i = i.xpath('./@src')
        # print(i[0])
        imgs.append(i[0])

    if not os.path.exists(path_3 + f'\\漫画\\{title}'):
        os.mkdir(path_3 + f'\\漫画\\{title}')

    if not os.path.exists(path_3 + f'漫画\\{title}\\{s_title}'):
        os.mkdir(path_3 + f'\\漫画\\{title}\\{s_title}')
    print(s_title + '  进入下载............................')
    re1.close()
    for i in imgs:
        i_1 = str(i).rsplit('/')[-1]
        #判断是否有改图片
        if not os.path.exists(path_3 + f'\\漫画\\{title}\\{s_title}\\{i_1}'):
            # 纠错下载失败的图片
            try:
                # 这个下载会卡死,使用有timeout的
                # req.urlretrieve(item['image'], 'C:\\Users\\me\\Desktop\\4k\\' + item['image'].rsplit('/', 1)[-1])
                Down_img(IP, H_2, i, s_title, title, i_1)
            except:
                Down_img(IP, H_2, i, s_title, title, i_1)

            print(i_1)
        # sleep(random.random()*5)


if __name__ == '__main__':
    # url = 'https://cn.godamanga.com/manga/butiange-xiada/0_101/'
    # Save_image(url)
    Headers, Ips, H = Analysis()
    response = Analysy(Headers, Ips)
    urls_name, title = Analysy_1(response)

    pool = ThreadPoolExecutor(10)
    for key, value in urls_name.items():
        pool.submit(Save_image, key, value, title, Headers, Ips, ch(H))
        # Save_image(key, value, title, Headers, Ips, ch(H))
        sleep(10)
    pool.shutdown(wait=True)
    print('         下载完成       \n')
