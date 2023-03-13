import threading
import time

"""
    用装饰器实现多线程
"""
import parsel
import requests

urls = [
    'https://maoyan.com/board/4?offset=0',
    'https://maoyan.com/board/4?offset=10',
    'https://maoyan.com/board/4?offset=20',
    'https://maoyan.com/board/4?offset=30',
    'https://maoyan.com/board/4?offset=40',
    'https://maoyan.com/board/4?offset=50',
    'https://maoyan.com/board/4?offset=60',
    'https://maoyan.com/board/4?offset=70',
    'https://maoyan.com/board/4?offset=80',
    'https://maoyan.com/board/4?offset=90',
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}


def decorator(func):
    def wrapper(*args, **kwargs):
        # func 是顺序运行
        # 在函数运行的时候,将其变成多线程的
        # ret = func(*args, **kwargs)
        # return ret
        # func(*args, **kwargs)
        threading.Thread(target=func, args=args, kwargs=kwargs).start()

    return wrapper


@decorator
def download(url):
    response = requests.get(url, headers=headers)
    sel = parsel.Selector(response.text)
    title = sel.css('.name a::text').get()
    print(url, title)


if __name__ == '__main__':
    start_time = time.time()
    for url in urls:
        download(url)
        # thread1 = threading.Thread(target=download, args=(url,))
        # thread1.start()
    while len(threading.enumerate()) > 1:
        pass
    print('time:', time.time() - start_time)
