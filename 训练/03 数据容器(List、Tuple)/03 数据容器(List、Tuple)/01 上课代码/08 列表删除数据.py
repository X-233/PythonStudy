list1 = ['a', 'e', 'b', 'c', 'd', 'e', 'f']

# pop()     默认删除最后一个元素
# list1.pop()
# list1.pop(2)  # # pop() 可以指定位置进行删除, 根据下标删除数据

# res = list1.pop(2)  # 会返回删除的数据, pop --> 弹出
# print(res)


# 注意是指定元素, 不是指定列表的下标, 仅会删除第一次出现的数据
# list1.remove('e')
#
# print(list1)

# del作用与内存删除
del list1[0]

print(list1)