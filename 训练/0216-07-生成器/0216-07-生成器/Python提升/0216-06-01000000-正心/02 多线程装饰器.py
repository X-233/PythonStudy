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


def download(url):
    response = requests.get(url, headers=headers)
    sel = parsel.Selector(response.text)
    title = sel.css('.name a::text').get()
    print(url, title)


if __name__ == '__main__':
    start_time = time.time()
    for url in urls:
        thread1 = threading.Thread(target=download, args=(url,))
        thread1.start()
    while len(threading.enumerate()) > 1:
        pass
    print('time:', time.time() - start_time)

