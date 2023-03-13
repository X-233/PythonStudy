"""
    自定义一个生成器对象 MyRange
    可以从 a-z 循环迭代三次之后结束
"""


class MyRange:
    def __init__(self, start, end):
        self.start = ord(start)
        self.end = ord(end)

        # 记录当前生成到第几个数字了
        self.curr = self.start
        self.times = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr <= self.end:
            item = self.curr
            self.curr += 1
            return chr(item)
        else:
            if self.times < 3:
                self.times += 1
                # 次数没有超过三次,重置一下起始值
                self.curr = self.start
                item = self.curr
                self.curr += 1
                return chr(item)

        raise StopIteration


my_range = MyRange('a', 'z')
for item in my_range:
    print(item)
