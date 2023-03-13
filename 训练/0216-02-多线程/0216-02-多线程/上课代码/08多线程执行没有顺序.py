import threading
import time
import random

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


def download(url, index):
    time.sleep(random.random())
    print(index, url)


index = 1
for url in urls:
    # download(url)
    t1 = threading.Thread(target=download, args=(url, index), kwargs={})
    t1.start()  # 启动线程对象
    index += 1

"""
    多线程运行是没有顺序的
    
    但是可以对线程进行编号, 然后对结果进行排序
    
    ctrl + alt + l 快速格式化
"""
