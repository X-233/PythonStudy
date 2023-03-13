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
    print(url)
    return url


def process_request(url_list2):
    # 进程处理的逻辑
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    for url in url_list2:
        thread_pool.submit(download_page, url)


if __name__ == '__main__':

    start_time = time.time()
    thread_pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    # 把每一个任务都丢到进程里面
    # 将 100 个任务等分 5 10 20 份都可以
    # for url in url_list:
    for i in range(20, 101, 20):
        thread_pool.submit(process_request, url_list[i - 20:i])

    thread_pool.shutdown()
    print('进程池运行的时间:', time.time() - start_time)

"""
    100 个任务  每个任务需要 1s 中
    顺序执行  100 * 1s = 100s
    
    5个线程  100/5 * 1s = 20s
    5个进程  100/5 * 1s = 20s
    
    5个进程 + 每个进程开5线程  100 / 5 / 5 * 1s = 4s 
"""
