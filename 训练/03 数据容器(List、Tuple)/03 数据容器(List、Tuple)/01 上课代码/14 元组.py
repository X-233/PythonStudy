# 元组是一种不可变的数据类型

# 一旦定义了一个元祖, 里面的值是不能被修改的
# 增删改查, 只支持数据查找

tup1 = (1, 2, 3, 4)
# 查看元组的数据类型
print(tup1)
print(type(tup1))

# 列表中所有数据查找方法元组都支持
print(tup1[2])
print(tup1[1:-1])
print(tup1.index(3))
print(tup1.count(3))
print(len(tup1))
print(1 in tup1)

# 不支持修改
# tup1[0] = 100

#
# 创建只有一个数据的元组
# 在元组的一个元素后面加一个逗号
tup1 = (12.5, )
print(tup1)
print(type(tup1))