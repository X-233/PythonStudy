"""（选做题）
打印一百以内的素数
素数定义为在大于1的自然数（到无穷大的整数）中，除了1和它本身以外不再有其他因数。

1. 打印0-100的所有数字
2. 判断当数字是否是素数
    如果是素数就打印
    如果不是素数就什么都不做
"""
sum_1 = 100
while sum_1:
    i_1 = sum_1 % 2
    i_2 = sum_1 % 3
    i_3 = sum_1 % 5
    i_4 = sum_1 % 7
    if i_1 and i_2 and i_3 and i_4:
        print(sum_1)
    elif sum_1 == 2 or sum_1 == 3 or sum_1 == 5 or sum_1 == 7:
        print(sum_1)
    sum_1 -= 1
