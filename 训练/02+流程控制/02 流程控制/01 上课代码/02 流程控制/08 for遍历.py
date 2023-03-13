
"""for遍历"""
# for i in 'abcdefg':
#     print(i)

# 所有的数据容器都能遍历
# for i in ['aa', 'bb', 'cc']:
#     print(i + '999')

"""range"""
# range() 函数可创建一个整数列表，一般用在 for 循环中。
"""
- start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
- stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
- step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""# [1, 10)
# range(起始值, 结束值)  范围区间是一个左闭右开的区间, 顾首不顾尾
print(list(range(1, 10)))
print(list(range(1, 10, 1)))  # range(起始值, 结束值, 步长)   步长默认为1, 可以省略
print(list(range(1, 10, 2)))  # 步长表示在数据范围内怎么取值
print(list(range(-1, -10, -2)))  # 逆序指定步长为负数就可以了, 范围也要逆序取值
# 123456789
# 不可迭代对象 --> 面向对象


# range() 函数可创建一个整数列表，一般用在 for 循环中
# for i in range(1, 11, 2):
#     print(i)

for i in range(11):  # range 只传一个数字就是 0 到这个数字的范围区间
    print(i)

