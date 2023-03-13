# 假设目前系统中有如下学生
students = [
    {'name': '丸子', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '欧阳吹雪', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '巳月', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
]

# 要根据学生的名字做信息查询
# 用户输入需要查询的学生名字
name = input('请输入您要查询的学生姓名:')

# 先遍历所有学生
for stu in students:
    # 如果输入的学生名字等于学生信息列表中某个学生名字, 就代表找到了这个学生
    if name == stu['name']:
        print('姓名\t语文\t数学\t英语\t总分')
        print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
        break

# 找完学生信息列表中的学生, 都没有找到, 就会走else代码逻辑
else:
    print('该学生不存在, 请检查名字是否输入正确!')

