import threading
import time

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


def download(url):
    # print('下载文件开始...')
    print(url)
    # 延时从操作
    time.sleep(1)
    # print('下载文件完毕...')


for url in urls:
    # download(url)
    t1 = threading.Thread(target=download, args=(url,), kwargs={})
    t1.start()  # 启动线程对象
