import threading
import time
import queue


def producer(pipeline):
    """生产者 厨师做包子"""
    for i in range(1, 10000):
        time.sleep(1)
        print('做出了第{}个包子'.format(i))
        pipeline.put(f'第{i}个包子')


def consumer(pipeline):
    """消费者 吃包子"""
    while True:
        time.sleep(3)
        message = pipeline.get()
        print('消费者吃了{}'.format(message))


if __name__ == '__main__':
    pipeline = queue.Queue(maxsize=10)  # 队列的容量可能会满
    # 队列的实现方式有很多种
    threading.Thread(target=producer, args=(pipeline,)).start()
    threading.Thread(target=producer, args=(pipeline,)).start()
    threading.Thread(target=consumer, args=(pipeline,)).start()
