# 集合: 可变的 不可重复的(去重) 无序的 数据类型

char1 = 'hello '
char2 = 'world !'
char3 = char1 + char2  # 字符串是不可变的, 但是字符串相加返回的是一个新的对象
print(char3)

arr1 = [1, 2]
arr2 = [3, 4]

print(arr1 + arr2)  # 列表相加返回的是一个新的对象
print('arr1:\t', arr1)
print('arr1 * 4:\t', arr1 * 4)
arr1.extend(arr2)  # 修改原有的列表
print('arr1:\t', arr1)
