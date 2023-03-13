list1 = [1, 2, 3, 4, 5]

import functools  # 内置模块

def func(a, b):
    return a / b

# reduce 累积运算的方法
result = functools.reduce(func, list1)
print(result)