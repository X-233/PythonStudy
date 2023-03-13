import concurrent.futures
import random
import threading
import time

import requests

url_list = ['http://www.baidu.com?page={}'.format(page) for page in range(100)]


def download_page(url):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    # }
    # response = requests.get(url, headers=headers)

    # 会有一个延时
    # 返回的网页会被加载到内存当中
    time.sleep(0.0001)
    return url


if __name__ == '__main__':
    start_time = time.time()
    for url in url_list:
        download_page(url)
    print('默认运行的时间:', time.time() - start_time)

    start_time = time.time()
    # 1. 创建线程池
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    for url in url_list:
        # download_page(url)
        # 非常不推荐 会启动太多的线程
        # threading.Thread(target=download_page, args=(url,)).start()
        # (函数名, 参数1,参数2,....)
        thread_pool.submit(download_page, url)

    thread_pool.shutdown()  # 等待线程池里面的任务全部执行完毕
    print('线程池运行的时间:', time.time() - start_time)

    start_time = time.time()
    # 1. 创建线程池
    thread_pool = concurrent.futures.ProcessPoolExecutor(max_workers=10)
    for url in url_list:
        # download_page(url)
        # 非常不推荐 会启动太多的线程
        # threading.Thread(target=download_page, args=(url,)).start()
        # (函数名, 参数1,参数2,....)
        thread_pool.submit(download_page, url)

    thread_pool.shutdown()  # 等待线程池里面的任务全部执行完毕
    print('进程池运行的时间:', time.time() - start_time)

"""
    100 任务,不管在哪里等,都是等  
    io 密集型任务  网页服务器
    
    顺序执行: 一个一个的等
    多线程执行: 全部在一起等
    多进程执行: 在不同的房间里面等  (创建进程的时候,会有资源的开销)
"""
