"""运算符的使用"""

"""算术运算符"""
three = 3
ten = 10

# 10 取余 3 等于 1
print(ten % three)

# 10 取整 3 等于 3
print(ten // three)

# 10 的 3 次幂   = 10 x 10 x 10
print(ten ** 5)

"""赋值运算符"""
print('-----------------------------------------------------')
# ten = ten + three
# print(ten)

ten -= three  # 两个变量相加, 通过赋值运算把结果赋给左边的变量
print(ten)