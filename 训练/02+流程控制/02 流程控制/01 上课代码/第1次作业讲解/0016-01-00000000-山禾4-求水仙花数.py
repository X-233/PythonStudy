"""
选做:
    请找出 100-999 之间的所有水仙花数
"""
for i in range(100, 1000):
    # print(i)
    g = i % 10

    s = i // 10 % 10

    b = i // 100

    result = g ** 3 + s ** 3 + b ** 3
    # print(result)

    if i == result:
        print(i, '是水仙花数')
