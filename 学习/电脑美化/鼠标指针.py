# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import parsel
import requests
import os
from concurrent.futures import ThreadPoolExecutor

def header():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    return headers

def analysis(url_2):
    html = requests.get(url=url_2, headers=header())
    select = parsel.Selector(html.text)
    # print(html.status_code)

    list_1 = select.xpath('//li[@class="post-list-item item-post-style-12"]')
    list_2 = [i.xpath('.//a[1]/@href').get() for i in list_1]
    next_page_url = select.xpath('//*[@id="primary-home"]/div[3]/ul/li[last()-1]/a/@href').get()

    return next_page_url, list_2

def analysis2(url_3):
    html = requests.get(url=url_3, headers=header())
    select = parsel.Selector(html.text)
    url = select.xpath('//span[@class="lianai qiye"]')[1].xpath('./a/@href').get()
    title = select.xpath('//strong/text()').get()
    print('正在下载: ' + title)
    con = requests.get(url=url, headers=header()).content
    with open(title + '.rar', 'wb')as f:
        f.write(con)
    print('下载完成: ' + title)

if __name__ == '__main__':
    url_1 = 'https://zhutix.com/tag/cursors'
    if not os.path.exists('美化'):
        os.mkdir('美化')
        os.chdir('美化')
    url_list_1 = []
    url_list_2 = []

    while url_1:
        url_list_1.append(url_1)
        url_1, url_list2 = analysis(url_1)
        url_list_2.extend(url_list2)

    pool = ThreadPoolExecutor(3)
    for i in url_list_2:
        pool.submit(analysis2, i)
    pool.shutdown(wait=True)

