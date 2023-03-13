# 有序的数据类型: 字符串\列表\元组

str1 = 'abcdefg'

result = list(str1)
print(result)
print(type(result))

result2 = tuple(result)
print(result2)
print(type(result2))

result3 = str(result2)
print(result3)
print(type(result3))

print(list('[[1, 2, 3], [4, 5, 6]]'))
print(eval('[[1, 2, 3], [4, 5, 6]]'))
# eval 将字符串转成Python对象