import queue

# 1. 创建一个队列
q = queue.Queue(maxsize=10)  # 设置队列的容量最大为 10

# 2. 往队列里面添加数据
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)
q.put(7)
q.put(8)
q.put(9)
q.put(10)
# q.put_nowait(11)  # 放入的时候不进行等待
q.put(11, block=True, timeout=3)  # 超出了队列的容量之后就会一直阻塞 等待. 直到队列里面有空元素时再次放入
# timeout 等待时间
print(q.qsize())  # 获取队列的大小

# 3. 从队列里面取出数据
for i in range(10):
    print(q.get())
print(q.get())  # 获取数据 如果没有就会一直阻塞 等待 直到队列里面有内容加入是,就立马取出
