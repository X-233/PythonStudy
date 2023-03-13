import multiprocessing
import threading
import time
import os


def list_append(arr):
    arr.put(1)
    arr.put(2)
    arr.put(3)
    print(os.getpid(), arr.qsize())


if __name__ == '__main__':
    arr = multiprocessing.Queue(maxsize=10)  # 队列里面最多容纳 10 个元素

    multiprocessing.Process(target=list_append, args=(arr,)).start()
    multiprocessing.Process(target=list_append, args=(arr,)).start()
    time.sleep(1)
    """
        多进程数据不共享的原因: 多进程环境是隔离的
        多进程数据共享就需要用队列或则是数据库实现进程间通信
    
    """
    print(os.getpid(), arr.qsize())
    print([arr.get() for item in range(6)])
"""
    硬件 cpu 6核6线程  cpu运行的时候会尽力的均衡每个核心的任务
    
    软件 我的程序 开启了12个进程
    
    多线程/多进行都可以并发    多进程才能并行
    
    硬件才有核心, 软件是没有核心的. 软件只会用到算力/内存
    
    
    多线程会有竞争的问题,引发数据错乱
    多进程数据不共享,会有进程间通信的问题
"""