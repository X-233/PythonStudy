import time
import threading  # 多线程模块


def work():
    print('5. 洗茶杯：1min')
    time.sleep(1)
    print('6. 放茶叶：1min')
    time.sleep(1)


# time.sleep(1)  # 延时 1s
start_time = time.time()
print('1. 洗壶: 1min')
time.sleep(1)
print('2. 灌凉水：1min')
time.sleep(1)
print('3. 烧水：1min')
time.sleep(1)
print('4. 等水烧开：3min')
threading.Thread(target=work).start()  # 等待的时候去做其他的任务
time.sleep(1)
time.sleep(1)
time.sleep(1)
# 5 6 需要请一个帮手 帮我们去做
# print('5. 洗茶杯：1min')
# time.sleep(1)
# print('6. 放茶叶：1min')
# time.sleep(1)
# 多线程在做事情的时候需要将任务打包为一个函数对象
# work()
# threading.Thread(target=work).start()  # 写在后面的话就是等待完之后再去做
print('7. 泡茶：1min')
time.sleep(1)
print('总运行时间:', time.time() - start_time)
