
"""布尔类型"""
# <class 'bool'>  布尔类型
# 布尔类型的数据中只有 True 和 False 两种结果(两级分化最严重, 走极端)
# True  真/对
# False  假/错

true = True
false = False

print(true)
print(type(true))
print('--------------布尔类型的隐式转化-----------------')
# 布尔类型在表达式中, 会在底层经过 隐式转化<看不到>, 转化成一个布尔判断的结果
print(0 > 5)

if 5 > 0:  # 在后续学习的判断条件中, 会把条件转化成布尔结果, 只有结果为True的时候才会执行判断下面的逻辑
    print('表达式为真')

print('---------布尔类型可以在Python中任意的类型中判断结果')
print('----------------------str----------------------')
# # 字符串类型, 除了 空字符串 布尔值全部是 True
print(bool(''))
print(bool(' '))
print(bool('fhreiohang'))

print('----------------------int float----------------------')
# 数值类型 除了 0 之外布尔值全部是 True
print(bool(0))
print(bool(-100))
print(bool(100))
print(bool(0.2))

