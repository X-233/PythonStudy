import time

import requests


def get_html(url):
    response = requests.get(url)
    return response.text


def save_html(html, name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(html)


"""把函数当做参数使用"""


def wrapper(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(time.time() - start)
    return result


print('----------------------------------------------------------------')
html = wrapper(get_html, 'http://www.baidu.com')
wrapper(save_html, html, 'baidu.html')

html = wrapper(get_html, 'http://www.360.com')
wrapper(save_html, html, '360.html')

html = wrapper(get_html, 'http://www.soso.com')
wrapper(save_html, html, 'soso.html')

"""闭包装饰对象"""


def decorator(func):
    # 利用闭包的原理 缓存 func
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result

    return wrap


print('----------------------------------------------------------------')
dec_get = decorator(get_html)  # get_html 传递给了 func
dec_save = decorator(save_html)
# dec_get 返回回来的装饰过的函数
# html = wrapper(get_html, 'http://www.baidu.com')
html = dec_get('http://www.baidu.com')
# wrapper(save_html, html, 'baidu.html')
dec_save(html, 'baidu.html')

html = dec_get('http://www.360.com')
dec_save(html, '360.html')

html = dec_get('http://www.soso.com')
dec_save(html, 'soso.html')
