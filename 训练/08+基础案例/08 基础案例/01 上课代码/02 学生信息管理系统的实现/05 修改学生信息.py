# 假设目前系统中有如下学生
students = [
    {'name': '丸子', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '欧阳吹雪', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '巳月', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
]

name = input('请输入您要修改的学生姓名:')

# 先遍历所有学生
for stu in students:
    # 如果输入的学生名字等于学生信息列表中某个学生名字, 就代表找到了这个学生
    if name == stu['name']:
        print('(如果输入为空,就使用原来的)')
        name_ = input('请输入修改学生的名字:')
        chinese = input('请输入修改学生的语文成绩:')
        math = input('请输入修改学生的数学成绩:')
        english = input('请输入修改学生的英语成绩:')
        # total = chinese + math + english

        if name_:
            stu['name'] = name_
        if chinese:
            stu['chinese'] = int(chinese)
        if math:
            stu['math'] = int(math)
        if english:
            stu['english'] = int(english)

        stu['total'] = stu['chinese'] + stu['math'] + stu['english']
        break

else:
    print('该学生不存在, 请检查名字是否输入正确!')

import pprint

pprint.pprint(students)