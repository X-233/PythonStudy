"""打印直角三角形
*
**
***
****
*****
"""
# print('*' * 3)

# i = 1
# while i < 6:
#     print('*' * i)
#     i +=1

# 不能使用字符串的乘法，循环打印直角三角形
# j = 1
# while j <= 3:
#     print('*', end='')
#     j += 1

# 用循环嵌套打印 5 行小星星
i = 1
while i < 6: # 12345 -->对应的是5行, 控制的是外层循环的次数
    # print('正在执行外层循环:', i)

    """内层循环"""
    j = 1
    while j <= i:
        print('*', end='')
        # print('内层循环:', j)
        j += 1

    print()  # 作用: 在外层循环换行
    i += 1

