"""
    实现一个函数，每一次启动代码时就会生成一个 0-10 的随机值
    生成的随机值可以重复使用，等到下次启动代码时，又会生成一个新的随机数，直到程序结束。
    同时这个随机数在程序运行中不允许被修改

    每次启动程序之后都会生成一个随机数，在代码运行过程中可以一直使用。每次调用时使用的是程序启动时生成的随机数，而不是每次都会生成。
"""

import random
import pprint


def random_int():
    # 2. 生成一个随机值
    num = random.randint(0, 10)

    # 3. 在函数内部定义一个猜数字的逻辑,并发挥结果
    def guss_int():
        # 6. 执行猜数字的逻辑, 然后返回结果
        num2 = int(input('请输入一个数字:'))
        if num2 == num:
            return '恭喜你猜对了'
        elif num2 > num:
            return '太大了'
        elif num2 < num:
            return '太小了'

    # 4. 返回猜数字函数对象
    return guss_int


# 1. 调用外部函数
guss = random_int()
ret = ''
while ret != '恭喜你猜对了':  # 7. 如果没有猜对,就继续玩游戏
    ret = guss()  # 5. 调用猜数字的函数,进行猜数字的逻辑
    print(ret)

guss2 = random_int()  # 调用函数,创建一个随机值

pprint.pprint(globals())
