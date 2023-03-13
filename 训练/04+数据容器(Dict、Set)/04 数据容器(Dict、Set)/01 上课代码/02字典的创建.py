# 定义: 字典是一种可变的、无序的、键值对的、复杂的数据容器

"""
{}      大括号就是字典的创建符号
<class 'dict'>  字典类型

字典中数据的形式都是键值对的形式 key: value
    key: value  键值对之间用英文的冒号隔开
    key  -->
            冒号左边是一个键,
            键可以是: 字符串/数字/元祖/布尔类型, 列表等可变的数据类型不能作为键
            键必须是唯一的
            (推荐用字符串作为键)
    value -->
            冒号右边可以是任意类型
"""

person = {
    'name': '正心',
    'gender': '男',
    'age': 18,
    True: True,
    ('',): ('',),
    1: [],
    # []: ''
}
print(type(person))
print(person)

# TypeError: unhashable type: 'list'
# unhashable 不可哈希类型 --> 可变的数据类型 --> 列表 字典 集合
# 可哈希 --> 不可以改变的数据类型 --> 字符串 元祖 数字

# 有序的数据类型特点: 下标取值, 可以切片
# 字典是无序的, 不能根据下标取值
print(person['name'])
print(person['age'])
print(person[1])
print(person[True])

# 推荐用字符串作为键
