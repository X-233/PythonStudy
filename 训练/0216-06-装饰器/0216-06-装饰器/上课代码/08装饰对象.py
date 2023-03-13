import random
import time

import requests


def get_html(url):
    response = requests.get(url)
    return response.text


def save_html(html, name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(html)


"""闭包装饰对象"""


def decorator(func):  # 装饰的效果就是用来计算函数运行的时间
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result

    return wrap


dec_get = decorator(get_html)
dec_save = decorator(save_html)

html = dec_get('http://www.baidu.com')
dec_save(html, 'baidu.html')


# 可以用装饰器计算 add 函数运行的时间吗 ?
def add(x, y):
    time.sleep(random.random())
    return x + y


dec_add = decorator(add)
dec_add(1, 2)
