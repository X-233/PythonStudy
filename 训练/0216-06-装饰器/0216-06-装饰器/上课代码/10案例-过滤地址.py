"""
    过滤下列一串网址中不属于猫眼的网址
"""
urls = [
    'https://maoyan.com/board/4?offset=0',
    'https://maoyan.com/board/4?offset=10',
    'https://maoyan.com/board/4?offset=20',
    'https://maoyan.com/board/4?offset=30',
    'https://www.baidu.com',
    'https://www.sohu.com',
    'https://maoyan.com/board/4?offset=40',
    'https://maoyan.com/board/4?offset=50',
]

import requests


def filter_url(func):
    def wrapper(*args, **kwargs):
        # 在被装饰的函数调用之前进行过滤
        # print('被装饰函数调用之前', args, kwargs)
        if 'maoyan.com' not in kwargs['url']:  # 如果 url 地址当中没有猫眼的域名
            return f'不符合要求的地址: {url}'
        result = func(*args, **kwargs)
        return result

    return wrapper


@filter_url
def download_maoyan(url):
    response = requests.get(url)
    return response.url


for url in urls:
    url = download_maoyan(url=url)
    print(url)
