""""""
import json

str_info = """**************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 修改学生信息
5. 删除学生信息

0. 退出系统
**************************************************"""
with open('students.json', mode='r', encoding='utf-8') as f:
    students_str = f.read()

students = json.loads(students_str)

while True:
    print(str_info)
    action = input('请选择你想要进行的操作:')
    if action == '1':
        print('1. 新建学生信息')
        name = input('请输入学生的姓名:')
        chinese = int(input('请输入学生的语文成绩:'))
        math = int(input('请输入学生的数学成绩:'))
        english = int(input('请输入学生的英语成绩:'))
        total = chinese + math + english
        stu = {"name": name, "chinese": chinese, "math": math, "english": english, "total": total}
        students.append(stu)

    elif action == '2':
        print('2. 显示全部信息')
        print('姓名\t语文\t数学\t英语\t总分')
        for stu in students:
            print("{}\t{}\t\t{}\t\t{}\t\t{}".format(stu['name'], stu['chinese'], stu['math'], stu['english'],
                                                    stu['total']))

    elif action == '3':
        print('3. 查询学生信息')
        name = input('请输入你想要查询的学生姓名:')

        for stu in students:
            if name == stu['name']:
                print('姓名\t语文\t数学\t英语\t总分')
                print("{}\t{}\t\t{}\t\t{}\t\t{}".format(stu['name'], stu['chinese'], stu['math'], stu['english'],
                                                        stu['total']))

                break
        else:
            print('该学生不存在,请检查名字是否输入正确')

    elif action == '4':
        print('4. 修改学生信息')
        name = input('请输入你想要修改的学生姓名:')
        for stu in students:
            if name == stu['name']:
                print('(如果输入为空,就使用原来的)')
                name = input('请重新输入学生的名字:')
                chinese = input('请重新输入学生的语文成绩:')
                math = input('请重新输入学生的数学成绩:')
                english = input('请输重新入学生的英语成绩:')
                total = chinese + math + english
                if name:
                    stu['name'] = name
                if chinese:
                    stu['chinese'] = int(chinese)
                if math:
                    stu['math'] = int(math)
                if english:
                    stu['english'] = int(english)
                stu['total'] = stu['chinese'] + stu['math'] + stu['english']
                break
        else:
            print('该学生不存在,请检查名字是否输入正确')

    elif action == '5':
        print('5. 删除学生信息')
        name = input('请输入你想要删除的学生姓名:')
        for stu in students:
            if name == stu['name']:
                students.remove(stu)
                break
        else:
            print('该学生不存在,请检查名字是否输入正确')

    elif action == '0':
        print('0. 退出系统')
        with open('students.json', mode='w', encoding='utf-8') as f:
            students_str = json.dumps(students, ensure_ascii=False)
            print(students_str)
            f.write(students_str)
        break
    else:
        print('请输入正确的选择')

