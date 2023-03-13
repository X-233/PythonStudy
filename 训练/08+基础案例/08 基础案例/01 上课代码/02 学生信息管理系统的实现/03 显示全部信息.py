# 假设目前系统中有如下学生
students = [
    {'name': '丸子', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '欧阳吹雪', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '巳月', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
]
print('姓名\t语文\t数学\t英语\t总分')
for stu in students:
    print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')

