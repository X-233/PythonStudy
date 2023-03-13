# 定义: 字典是一种可变的、无序的、键值对的、复杂的数据容器

person = {
    'name': '正心',
    'position': '讲师',
    'gender': '男',
    'age': 19,
    'school': '青灯教育',
    'hobby': ['上课', '解答'],
}

print(person['name'])
# del person['name']
# print(person['name'])  # dict['key'] 取值, 如果键值对不存在就会报错

print('姓名:\t', person.get('name', None))
print('姓名:\t', person.get('name', '默认值'))
print('姓名:\t', person.get('name', '名字不存在'))

# 老师比方有 name1，name2，name3，我想取只要有 name 的都要

""".keys() 获取所有的键"""
print(person.keys())  # 字典的键是类似一个列表
print(list(person.keys()))
# .values 获取所有的值
print(person.values())

# .items() 获取所有的键值对
print(person.items())

for key in person.keys():
    print('key:\t', key)
    print('value:\t', person[key])
    print('item:\t', (key, person[key]))

print('--------------')
print(person.items())
for key, value in person.items():
    print(key, value)
