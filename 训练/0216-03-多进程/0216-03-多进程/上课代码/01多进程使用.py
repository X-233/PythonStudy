import time
import threading
import multiprocessing


def upload():
    print("开始上传文件...")
    time.sleep(1)
    print("完成上传文件...")


def download():
    print("开始下载文件...")
    time.sleep(1)
    print("完成下载文件...")


# upload()
# download()

# threading.Thread(target=upload).start()
# threading.Thread(target=download).start()

if __name__ == '__main__':
    # 进程创建的时候会将主进程所有的数据全部拷贝一份
    multiprocessing.Process(target=upload).start()
    multiprocessing.Process(target=download).start()

    # python 没有程序的入口一说, 因为每个函数都可以单独运行
