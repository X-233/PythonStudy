import multiprocessing

import concurrent.futures

baidu_urls = ['https://www.baidu.com/?page=1', 'https://www.baidu.com/?page=2',
              'https://www.baidu.com/?page=3', 'https://www.baidu.com/?page=4',
              'https://www.baidu.com/?page=5', 'https://www.baidu.com/?page=6',
              'https://www.baidu.com/?page=7', 'https://www.baidu.com/?page=8',
              'https://www.baidu.com/?page=9', 'https://www.baidu.com/?page=10']

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
import requests


def get_html(url):
    response = requests.get(url)
    html = response.text
    return html


def save_html(html, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


def main(url, filename):
    html = get_html(url)
    save_html(html, filename)


def thread_pool(urls):
    print(urls)
    thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    for url in urls:
        page = url.split('?')[-1].split('=')[-1]
        filename = 'baidu_{}.html'.format(page)
        # 多进程与多线程出现问题不会直接报错
        thread_executor.submit(main, url, filename)


if __name__ == '__main__':
    # 进程池需要创建再最上面
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)

    # page = 1
    # for url in baidu_urls:
    #     filename = 'baidu_{}.html'.format(page)
    #
    #     # multiprocessing.Process(target=main, args=(url, filename)).start()
    #     # main(url, filename)
    #     executor.submit(main, url, filename)
    #
    #     page += 1

    executor.submit(thread_pool, baidu_urls[:5])
    executor.submit(thread_pool, baidu_urls[5:])
    # 如果是进程池嵌套线程池
