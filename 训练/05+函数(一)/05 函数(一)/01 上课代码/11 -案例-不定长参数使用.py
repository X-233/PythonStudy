"""
案例：
假设 python 中的 print 一次只能打印一个元素了

让我们自己实现 print 可以传递多个参数的功能。
"""


def print_2(*args, **kwargs):
    for i in args:
        print(i, end=' ')

    for j in kwargs.values():
        print(j, end=' ')


print_2(1, 2, 3, 4, 5, 90, 80, a=6, b=7, c=8, d=9, e='123')
