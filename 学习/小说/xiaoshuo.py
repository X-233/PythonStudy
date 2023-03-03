# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
# 小说下载
import csv
import os
import requests
from lxml import etree
from random import choice
import random
import re
from concurrent.futures import ThreadPoolExecutor
# from bs4 import BeautifulSoup


def H_IP():
    list_ip_port = []
    headers = []
    f = csv.reader(open(r'../../杂项/H.csv', encoding='utf-8'))
    #强制转换一下
    for i in list(f)[1:]:
        i1 = eval(i[0])
        headers.append(i1)
        i2 = eval(i[1])
        list_ip_port.append(i2)
    return headers, list_ip_port

def Analy(url):
    list_url = {}
    re1 = requests.get(url)
    re1 = re1.text
    re2 = etree.HTML(re1)

    # try:
    page = re2.xpath('//*[@id="allchapter_2"]/tr/td[5]/a/text()')[0]
    page = int((re.findall('\d+', page))[0])
    print(page)
    # except Exception as e:
    #     print(e)
    #     page = 1


    for i in range(page+1)[1:]:
        try:
            rand = int(random.random() * 99999999)
            re4 = requests.get(
                f'http://www.biquger.net/modules/article/wapallchapter.php?aid=2&page={i}&rand={rand}').text
            re4 = etree.HTML(re4)
            re5 = re4.xpath('//div')
            print(len(re5))
            for i in re5:
                text = i.xpath('./a/text()')[0]
                url = 'http://www.biquger.net' + i.xpath('./a/@href')[0]
                list_url[text] = url
        except Exception as e:
            print(e)

    return list_url
def Analysis(title, url, header, proxy):
    response = requests.get(url=url, headers=header, proxies=proxy, timeout=7)
    response.encoding = 'gbk'
    html = response.text
    text = etree.HTML(html)

    content = text.xpath('//*[@id="nr1"]/text()')
    con_list = []
    for i in content:
        if i != '\r\n':
            con_list.extend(i)
    # join转string
    content = ''.join(con_list)
    print(content)
    with open(f'C:\\Users\\me\\Desktop\\paqu\\小说\\{title}.txt', 'w', encoding='utf-8', newline='')as f:
        f.write(content)


if __name__ == '__main__':
    # url = input('请输入爬取的网址:    ')
    url = 'http://www.biquger.net/html/0/2/'
    H, IP = H_IP()
    url_list = Analy(url)
    pool = ThreadPoolExecutor(10)
    for key, value in url_list.items():
        if not os.path.exists(f'C:\\Users\\me\\Desktop\\paqu\\小说\\{key}.txt'):
            pool.submit(Analysis, key, value, choice(H), choice(IP))
    pool.shutdown(wait=True)
    print('#'*30+'         完成!!!')
