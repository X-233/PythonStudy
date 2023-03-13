# -*- coding: utf-8 -*-
"""
定义一个函数，对传入未知个长度的内容进行求和并且返回

传入的内容如下(print里面的东西)

"""

# print(1,2,3,4,5,a=6,b=7,c=8)

"""自己在下方编写代码实现功能"""

def fun1(*args, **kwargs):
    sum1 = 0
    for i in args:
        sum1 += i
    for i in kwargs.values():
        sum1 += i
    return sum1

if __name__ == '__main__':
    print(fun1(1, 2, 3, 4, 5, a=6, b=7, c=8))