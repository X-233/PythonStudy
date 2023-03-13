import time


def gen_1(n):
    index = 0
    ret = []
    while index < n:
        time.sleep(1)
        print('gen_1 延时1秒')
        ret.append(index * index)
        index += 1
    return ret


def gen_3(n):
    index = 0
    while index < n:
        time.sleep(1)
        print('gen_3 延时1秒')
        yield index * index  # yield 可以返回元素,然后再回调回来
        index += 1


for item in gen_1(4):
    print('gen1 ', item)

for item in gen_3(4):
    print('gen3 ', item)
