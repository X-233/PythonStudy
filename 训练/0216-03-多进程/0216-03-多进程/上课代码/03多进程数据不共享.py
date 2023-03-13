import multiprocessing
import threading
import time
import os


def list_append(arr):
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(os.getpid(), arr)


if __name__ == '__main__':
    arr = []
    # list_append(arr)
    # list_append(arr)

    # threading.Thread(target=list_append, args=(arr,)).start()
    # threading.Thread(target=list_append, args=(arr,)).start()

    multiprocessing.Process(target=list_append, args=(arr,)).start()
    multiprocessing.Process(target=list_append, args=(arr,)).start()
    time.sleep(1)
    print(os.getpid(), arr)
