import time

import requests


def get_html(url):
    response = requests.get(url)
    return response.text


def save_html(html, name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(html)


# html = get_html('http://www.baidu.com')
# save_html(html, 'baidu.html')
# 计算两个函数运行的时间

"""在外部添加代码实现效果"""
start = time.time()
html = get_html('http://www.baidu.com')
print('请求网页的时间', time.time() - start)
start = time.time()
save_html(html, 'baidu.html')
print('保存网页的时间', time.time() - start)

# 每一次写代码的时候都要计算时间

"""重新写一个函数实现时间的计算"""


def get_html2(url):
    start = time.time()
    response = requests.get(url)
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
