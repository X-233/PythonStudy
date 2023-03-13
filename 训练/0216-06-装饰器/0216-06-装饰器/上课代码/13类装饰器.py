import random
import time


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.func(*args, **kwargs)
        print('程序运行时间', time.time() - start)
        return ret


@Timer
def add(x, y):
    time.sleep(random.random())
    return x + y


# add = Timer(add)

print(add(1, 2))
print(add)

