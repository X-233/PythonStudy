import threading
import time
import random

number = 0


def add1():
    global number
    # 运行一百次加 1 运算
    for i in range(1000000):
        number += 1


def add2():
    global number
    # 运行一百次加 1 运算
    for i in range(1000000):
        # 无锁不安全的原因是因为敏感数据操作造成了覆盖
        number += 1  # 加法运算必须是一个整体


# add1()
# add2()
# print(number)
t1 = threading.Thread(target=add1)
t1.start()
t2 = threading.Thread(target=add2)
t2.start()

# .join 等待线程执行完毕在做后续的操作
t1.join()  # 多线程对象.join()  等待多线程执行完毕  字符串.join([])  合并字符串
t2.join()
print(number)  # 正常运行完应该两百万


# def add():
#     global number
#     number += 1
#
#
# import dis
#
# dis.dis(add)  # dis 可以看到 add 函数的汇编执行逻辑
"""
 38           0 LOAD_GLOBAL              0 (number)      # 锁定 number 的值
              2 LOAD_CONST               1 (1)           # 锁定需要加的常量
              4 INPLACE_ADD                              # 执行加法运算
              6 STORE_GLOBAL             0 (number)      # 存储运算的结果
              8 LOAD_CONST               0 (None)        # 释放常量
             10 RETURN_VALUE                             # 返回进行修改
             
cpu 一个核心 同时只能做一件事情
    人看起来可能同时在做很多件事情, 实际只有一件事情. 人的计算能力与 cpu 差距太大了
"""