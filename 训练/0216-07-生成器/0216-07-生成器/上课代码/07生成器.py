my_generator = (x * x for x in range(4))
print(list(my_generator))


def gen_1(n):
    index = 0
    ret = []
    while index < n:
        ret.append(index * index)
        index += 1
    return ret


print(gen_1(4))


class Gen2:
    def __init__(self, n):
        self.index = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
            ret = self.index * self.index
            self.index += 1
            return ret
        else:
            raise StopIteration


print(list(Gen2(4)))


def gen_3(n):
    index = 0
    while index < n:
        yield index * index  # yield 生成器
        index += 1


print(list(gen_3(4)))
