# 定义: 字典是一种可变的、无序的、键值对的、复杂的数据容器

person = {
    'name': '正心',
    'gender': '男',
    'age': 18,
}

print(person['name'])

# 如果指定一个字典中不存在的键进行赋值, 就会新增一个键值对
person['hobby'] = ['吃饭', '睡觉', '看代码']

# 如果键已经存在了, 就会覆盖这一个值
person['age'] = 19
print(person)

"""字典合并"""
# 语义化 information 信息
info = {'school': '青灯教育', 'position': '讲师', 'hobby': ['上课', '解答']}

# 将一个字典合并到另一个字典, 如果键相同, 就会进行覆盖
person.update(info)
print(person)
