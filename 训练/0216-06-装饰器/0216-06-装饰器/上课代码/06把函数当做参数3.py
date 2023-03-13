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


"""直接对函数进行时间计算"""


def wrapper_get_html(*args, **kwargs):
    start = time.time()
    result = get_html(*args, **kwargs)
    print('请求网页的时间', time.time() - start)
    return result


def wrapper_save_html(*args, **kwargs):
    start = time.time()
    result = save_html(*args, **kwargs)
    print('保存网页的时间', time.time() - start)
    return result


html = wrapper_get_html('http://www.baidu.com')
wrapper_save_html(html, 'baidu.html')

html = wrapper_get_html('http://www.360.com')
wrapper_save_html(html, '360.html')

"""把函数当做参数使用"""


def wrapper(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(time.time() - start)
    return result


print('----------------------------------------------------------------')
html = wrapper(get_html, 'http://www.baidu.com')
wrapper(save_html, html, 'baidu.html')
