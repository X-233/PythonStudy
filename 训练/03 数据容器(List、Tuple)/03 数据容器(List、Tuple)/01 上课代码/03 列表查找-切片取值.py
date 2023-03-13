"""列表是有序的数据容器"""
name_list = ['a', 'b', 'c', 'd', 'e', 'f']

"""
格式：

`[起始值:结束值:步长]` 

- start:  起始索引，从0开始，-1表示结束 
- stop：结束索引
- step：步长，end-start，步长为正时，从左向右取值。步长为负时，反向取值
"""
# 切片石根据列表索引进行切片的, 切片的范围也是左闭右开的区间
print(name_list[1:4])
print(name_list[0:3])
print(name_list[:3])  # 起始索引为0, 可以省略
print(name_list[1:6])
print(name_list[1:])  # 如果从一个数据开始后续的数都要, 那么可以不指定结束索引
print(name_list[1:5])
print(name_list[1:-1])

"""步长"""
print(name_list[1::1])
print(name_list[1::])   # 步长默认为1, 可以省略
print(name_list[1::2])   # 步长默认为1, 可以省略


"""如果指定负数步长, 数据范围需要倒着指定<逆序>"""
print(name_list[1::-1])
print(name_list[0::-1])
print(name_list[-1:0:-1])
print(name_list[-1:0:-2])
print(name_list[1:6:-2])
print(name_list[1:-1:-2])


# 切片的特性: 能够取某个范围的数据

# 在python中所有有序列<索引>的数据类型都支持切片
# 字符串
print('abcdef'[1:-1])

print('abcdef'[0])
