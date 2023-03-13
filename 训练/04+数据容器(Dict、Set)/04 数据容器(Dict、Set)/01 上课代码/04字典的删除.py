# 定义: 字典是一种可变的、无序的、键值对的、复杂的数据容器

person = {
    'name': '正心',
    'position': '讲师',
    'gender': '男',
    'age': 19,
    'school': '青灯教育',
    'hobby': ['上课', '解答'],
}

# .pop 指定键弹出值
# value = person.pop('hobby')
# print(value)
# print(person)
# print(person.popitem())  # 随机弹出内容

del person['name']  # del 是一个关键字
# del person  # del 删除字典
print(person)
