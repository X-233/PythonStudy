# 集合: 可变的 不可重复的(去重) 无序的 数据类型

# set1 = set('hello world !')
# print(set1)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1)
print(type(set1))

# 新增数据
set1.add('a')
set1.add('b')
set1.add(True)
set1.add(False)
set1.update(['6', 5])
print(set1)

# 删除数据
set1.remove('6')
set1.remove('a')
print(set1)

set3 = set()

set3.add(1)  # 添加一个元素
set3.update([2, 3])  # update 更新一个容器
set3.update(('a', 'b'))  # update 更新一个容器
set3.update('cd')
set3.update({'aa': 'aaa'})
print(set3)
