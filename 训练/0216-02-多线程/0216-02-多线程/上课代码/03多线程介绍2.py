""""""
import time
import threading

"""同时上传与下载文件"""


def download():
    print('开始下载文件')
    time.sleep(1)
    print('完成下载文件')


def upload():
    print('开始上传文件')
    time.sleep(1)
    print('完成上传文件')


# upload()
# download()

threading.Thread(target=upload).start()
threading.Thread(target=download).start()
