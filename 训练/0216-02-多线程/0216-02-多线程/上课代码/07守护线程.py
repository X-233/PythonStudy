""""""
import time
import threading

"""同时上传与下载文件"""


def download():
    print('开始下载文件')
    time.sleep(3)
    print('完成下载文件')


# 如果想主线程结束的时候, 子线程全部被杀死
# daemon=True 开启守护线程
t1 = threading.Thread(target=download, daemon=True)  # 子线程对象
t1.daemon = True  # 第二种设置方法
t1.start()


# 默认的情况下, 主线程退出时 子线程不会被 kill
print('主线程运行结束了')
