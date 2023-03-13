import threading
import time
import random

urls = [
    f'https://www.baidu.com?page={page}' for page in range(100)
]
lock = threading.Lock()


def download(url):
    time.sleep(0.1)
    # lock.acquire()
    with lock:  # 使用上下文管理器操作锁, 操作完之后就会自动释放锁
        with open('demo.txt', mode='a', encoding='utf-8') as f:
            f.write(f'url:{url}\n')
    # lock.release()   # 加锁之后 忘记释放锁了 就会造成死锁
    # 死锁是忘记释放锁了, 是一个逻辑问题, 只能在写程序的时候尽量避免
    # 或者通过编写更完善的逻辑避免锁没有释放


for url in urls:
    download_thread = threading.Thread(target=download, args=(url,)).start()
