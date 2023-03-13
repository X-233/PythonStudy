import threading
import time
import random

# 1. 创建一把锁
lock = threading.Lock()
number = 0


def add1():
    global number
    for i in range(1000000):
        # 2. 进行加法操作之前上锁
        lock.acquire()
        number += 1
        # 3. 加法操作完之后释放锁
        lock.release()


def add2():
    global number
    for i in range(1000000):
        lock.acquire()
        number += 1
        lock.release()


t1 = threading.Thread(target=add1)
t1.start()
t2 = threading.Thread(target=add2)
t2.start()
t1.join()
t2.join()
print(number)
