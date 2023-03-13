"""
用for语句实现九九乘法表
"""

for i in range(1, 10):  #  控制行数 123456789
    for j in range(1, i + 1):  # 控制列数
        print(f'{j} * {i} = {i * j}', end='\t')
    print()

