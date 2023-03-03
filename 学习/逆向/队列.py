# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
import requests
from lxml import etree
import queue

if __name__ == '__main__':
    q = queue.Queue(maxsize=5)
    print(type(q))
    """
    queue.Queue(maxsize=0)：先进先出，最早进入队列的数据先出队列；
    queue.LifoQueue(maxsize=0)：最后进入队列的数据先出队列；
    PriorityQueue(maxsize=0)：比较队列中每个数据的大小，值最小的数据先出队列；
    queue.SimpleQueue：与 1 相似，只是一个简单队列，缺少一些高级的方法。
    """