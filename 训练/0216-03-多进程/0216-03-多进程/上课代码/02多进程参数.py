import time
import threading
import multiprocessing  # 多进程的模块名


def run_process(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    multiprocessing.Process(target=run_process, args=(1, 2, 3, 4, 5, 6),
                            kwargs={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}).start()
