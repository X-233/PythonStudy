"""
    自定义一个生成器对象 MyRange
    可以从 a-z 循环迭代三次之后结束
"""


def MyRange(i):
    while i < 3:
        x = [chr(j + ord('a')) for j in range(ord('z') - ord('a') + 1)]
        yield x
        i += 1

def MyRange_1(i_1):
    while i_1 < 3:
        for j in range(ord('z') - ord('a') + 1):
            yield chr(j + ord('a'))
        i_1 += 1

for i in MyRange(0):
    print(i)

for i in MyRange_1(0):
    print(i)
