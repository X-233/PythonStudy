# -*- coding: utf-8 -*-
"""
定义一个函数，对传入未知个长度的内容进行求和并且返回

传入的内容如下(print里面的东西)

"""

# print(1,2,3,4,5,a=6,b=7,c=8)

"""自己在下方编写代码实现功能"""


def add(*args, **kwargs):  # *args --> 接受所有的位置参数; **kwargs --> 接受所有的关键字参数
    # print(args)
    # print(kwargs)

    total = 0
    for arg in args:
        total += arg  # 把所有的位置参数求和

    for value in kwargs.values():
        total += value

    return total


result = add(1, 2, 3, 4, 5, 6, 7, a=6, b=7, c=8, d=9)
print(result)

add()

# result = add(1, 2, 3, 4, 5, 6, 7, a='6', b='7', c='8', d='9')