"""
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

判断 371 是不是水仙花数
"""

number = 371

g = number % 10
print(g)

s = number // 10 % 10
print(s)

b = number // 100
print(b)


result = g ** 3 + s ** 3 + b ** 3
print(result)

if number == result:
    print(number, '是水仙花数')
