"""
自定义实现完整的 range
"""


class MyRange(object):
    def __init__(self, start, stop, step):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        # 生成数据的规则
        self.start += self.step
        if self.start < self.stop:
            return self.start
        # 超出范围之后就不允许进行迭代
        # else:
        #     raise StopIteration
        return None


my_range = MyRange(1, 5, 1)
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))

# for item in my_range:
#     print(item)
#
print(list(my_range))
