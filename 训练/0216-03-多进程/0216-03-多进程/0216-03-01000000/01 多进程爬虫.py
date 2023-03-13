import time

import requests
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

baidu_urls = ['https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/']

def get_html(url_list, num_1):
    pool_1 = ThreadPoolExecutor(5)
    print(url_list)
    for j in url_list:
        pool_1.submit(save_html, j, (num_1 * 5) + url_list.index(j))

def save_html(url, num):
    response = requests.get(url=url)
    data = response.text
    print(data)
    with open('baidu_' + str(num) + '.html', mode='w', encoding='utf-8')as f:
        f.write(data)

if __name__ == '__main__':
    t_start = time.time()
    pool_2 = ProcessPoolExecutor(2)
    for i in range(2):
        pool_2.submit(get_html, baidu_urls[i * 5: (i+1)*5], i)
    pool_2.shutdown()
    print(time.time() - t_start)




""" 
    定义一个请求方法 get_html 用于并返回网页数据
    定义一个保存方法 save_html 用于保存返回的网页数据
    
    多进程请求 baidu_urls ，计算所有请求的时间
    然后去将每一个文件分别标号保存，保存文件名为
    baidu_1.html,baidu_2.html,baidu_3.html,
    baidu_4.html,baidu_5.html,baidu_6.html,
    baidu_7.html,baidu_8.html,baidu_9.html,
    baidu_10.html


如果不会爬虫, 可以参照下面的请求，也可以微信私聊正心
>>> import requests
>>> response = requests.get('https://www.baidu.com/')
>>> html = response.text
"""




