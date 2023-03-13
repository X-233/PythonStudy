"""
自定义一个 MyRange 类。实现 range 的功能。
但只接收两个参数，起始值与步长，实现无限增长(for 实现死循环)

__next__
__iter__
"""


class MyRange(object):
    def __init__(self, start, step):
        self.start = start - step
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        # 生成数据的规则
        self.start += self.step
        return self.start


my_range = MyRange(5, 2)
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
for item in my_range:
    print(item)
