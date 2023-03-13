# 定义: 字典是一种可变的、无序的、键值对的、复杂的数据容器

person = {
    'name': '正心',
    'name2': '正心老师',
    'name3': '青灯教育-正心老师',
    'nickname': '青灯教育-正心',
    'position': '讲师',
    'gender': '男',
    'age': 19,
    'school': '青灯教育',
}

# 老师比方有 name1，name2，name3，我想取只要有 name 的都要
for key in person.keys():
    if 'name' in key:
        print(key)

dict1 = {
    'name': '丸子',
    'age': 18,
    'gender': '女',
    '爱好': '吃喝玩乐'
}

print('--------------')
keys_list = ['height', 'name', 'weight', '爱好']
# 需求: 取出 keys_list 列表在 dict1 有的键对应的值
for key in keys_list:
    ret = dict1.get(key)
    if ret:
        print(f'{key}-{ret}')
