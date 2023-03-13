# 假设目前系统中有如下学生
students = [
    {'name': '丸子', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '欧阳吹雪', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '巳月', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
]

name = input('请输入您要删除的学生姓名:')

# 先遍历所有学生
for stu in students:
    # 如果输入的学生名字等于学生信息列表中某个学生名字, 就代表找到了这个学生
    if name == stu['name']:
        # 在学生信息列表中删除学生数据
        # pop 默认删除列表中最后一个数据, 可以指定索引删除列表中的数据  index
        students.remove(stu)
        break

else:
    print('该学生不存在, 请检查名字是否输入正确!')


import pprint

pprint.pprint(students)