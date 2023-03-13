"""
逻辑运算
    and --> 条件1 and 条件2 两个条件都成立,返回True,否则返回False
    or  --> 条件1 or  条件2 两个条件中的一个条件成立,就返回True
    not --> not 条件, 条件会直接逆转
"""
r = 5 > 4 and 6 > 9
print(r)
print(True and False)
print(True and True)
print('----------------------')
print(True or False)
print(False or True)
print(False or False)
print('------------------------')
print(not True)
print(not False)
# print(! False)
print('------------------------')
"""身份运算符"""
num1 = 123
num2 = 123
print(num1 is num2)  # is 左右链接两个对象, 判断这两个对象是不是同一对象, 基于内存地址判断的
print(id(num1))  # id() 查看对象内存地址
print(id(num2))
print('------------------------')
"""成员运算符"""
print('a' in 'vrkoavrsn')  # in 判断某个对象是不是属于另一个对象的部分, 一般在数据容器中判断
print('z' in 'vrkoavrsn')

