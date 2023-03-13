import time

import requests


def get_html(url):
    headers = {
        'user-agent': 'Chrome'
    }
    response = requests.get(url, headers=headers)
    return response.text


def save_html(html, name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(html)


"""重新写一个函数实现时间的计算"""


# 下面的函数是为了实现对象之前的函数进行计算时间
def get_html2(url):
    start = time.time()
    response = requests.get(url)  # 这一段逻辑是旧的代码
    print('请求网页的时间', time.time() - start)
    return response.text


def save_html2(html, name):
    start = time.time()
    with open(name, 'w', encoding='utf-8') as f:
        f.write(html)
    print('保存网页的时间', time.time() - start)


html = get_html2('http://www.baidu.com')
save_html2(html, 'baidu.html')

html = get_html2('http://www.360.com')
save_html2(html, '360.html')

"""直接对函数进行时间计算"""


def wrapper_get_html(url):
    start = time.time()
    # response = requests.get(url)  # 这一段逻辑是旧的代码
    html = get_html(url)  # 直接调用之前的函数得到结果, 不复制逻辑
    print('请求网页的时间', time.time() - start)
    return html


def wrapper_save_html(html, name):
    start = time.time()
    save_html(html, name)
    print('保存网页的时间', time.time() - start)


html = wrapper_get_html('http://www.baidu.com')
wrapper_save_html(html, 'baidu.html')

html = wrapper_get_html('http://www.360.com')
wrapper_save_html(html, '360.html')
