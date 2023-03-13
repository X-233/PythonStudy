"""
用for语句实现九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} x {i} = {j * i}', end='\t')
    print()