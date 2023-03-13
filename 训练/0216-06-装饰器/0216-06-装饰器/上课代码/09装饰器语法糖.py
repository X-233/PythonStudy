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


def timer(func):  # 装饰的效果就是用来计算函数运行的时间
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result

    return wrap


@timer  # 艾特谁就去找那个装饰器
def add(x, y):
    time.sleep(random.random())
    return x + y


# add = timer(add)  # decorator 给函数穿一件衣服就是装饰器
ret = add(1, 2)
print('ret', ret)
