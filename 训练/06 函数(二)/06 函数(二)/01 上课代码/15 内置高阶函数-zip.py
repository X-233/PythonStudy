a = [1, 2, 3]
b = [11, 22, 33]
c = [111, 222, 333, 444]

result = zip(a, b)
print(result)  # 组包返回的是一个zip对象 <zip object at 0x0000012FCDF5F080>, 可以强制转化或者遍历
print(list(result))  # 组合后类型是列表嵌套元组的数据类型

# 如果序列长度不一致, 按照最短的序列进行组包
result2 = zip(a, c)
print(list(result2))

result3 = zip(a, b, c)
print(list(result3))

str1 = '123456'
str2 = 'abcdef'
result4 = zip(str1, str2)
print(list(result4))

# 有序列数据 --> 有索引

res1 = (1, 2, 3)
res2 = ['a', 'b', 'c']
result5 = zip(res1, res2)
print(list(result5))