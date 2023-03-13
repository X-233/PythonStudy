import pprint

students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# def func(temp):
#     print('传进来的数据:', temp)
#     return temp['age']  # 函数的返回结果就是列表的排序规则
#
# # sort 方法中 key参数作用: 指定规则对列表数据进行排序
# # key 指定的函数对象, 会默认调用该函数对象, 可以把列表中所有的数据都传入到函数中
# students.sort(key=func)
#
# print('\n--------------------------------')
# pprint.pprint(students)

students.sort(key=lambda x:x['age'], reverse=True)
pprint.pprint(students)

