"""整型"""
one = 100

# 我们可以用 type() 函数, 查看变量的类型
# <class 'int'>  class表示一个类别, 'int': 表示类别的名字, 代表其类型是整型的数据类型
print(one)
print(type(one))


"""浮点型--> 小数"""
# <class 'float'> float --> 浮点型数据
two = 12.6
print(two)
print(type(two))

# 数值类型可以直接参数四则运算
print(one + two)

"""数值类型可以通过类型的关键字转化"""
print('----------------------------------------------')
print(int(two))
print(float(one))