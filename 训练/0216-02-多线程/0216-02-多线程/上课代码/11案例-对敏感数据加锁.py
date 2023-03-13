import threading
import time
import random

urls = [
    f'https://www.baidu.com?page={page}' for page in range(100)
]
lock = threading.Lock()


def download(url):
    # 等待的过程需要上锁吗 ?
    # lock.acquire()
    time.sleep(0.1)  # 大量的时间损耗是延时

    # 什么是敏感数据?  全局变量,多线程共同操作的变量/对象/文件
    lock.acquire()
    with open('demo.txt', mode='a', encoding='utf-8') as f:
        f.write(f'url:{url}\n')
    lock.release()


for url in urls:
    # download(url)
    download_thread = threading.Thread(target=download, args=(url,)).start()
    # 会直接创建 100 线程
"""
    加锁之后相比不加锁速度会慢一点点
    
    非敏感操作不加锁,就能享受到多线程加速的效果.
"""