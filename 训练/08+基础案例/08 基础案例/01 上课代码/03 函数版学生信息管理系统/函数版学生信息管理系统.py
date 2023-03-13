"""
1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
2. 用户用数字选择不同的功能(input)  1  2  3
3. 根据功能选择，执行不同的功能 (判断 多条件判断)
4. 需要记录学生的 姓名、语文成绩、数学成绩、英语成绩 、总分 (input, 考虑用数据容器存储学生信息, 针对整个系统也需要有一个容器存储所有学生数据)
5. 如果查询到指定的学生信息，用户可以选择 修改 或者 删除 信息
6. 进入或退出时加载或保存数据  (文件操作) 启动系统的时候需要加载这个系统的学生数据, 结束这个系统的时候需要保存所有的学生数据
"""

# 程序在运行的时候, 有没有同学知道这个程序什么时候结束?
# ATM  欢迎页面<提示插入磁卡> --> 用户插入磁卡后, 输入密码 --> 用户进行存取查款 --> 退卡  --> 等待下一个有缘人
import json
import pprint


def insert_student():
    """录入学生信息并且返回"""
    name_ = input('请输入学生的名字:')
    chinese = input('请输入学生的语文成绩:')
    math = input('请输入学生的数学成绩:')
    english = input('请输入学生的英语成绩:')

    stu = {}
    if name_:
        stu['name'] = name_
    if chinese:
        stu['chinese'] = int(chinese)
    if math:
        stu['math'] = int(math)
    if english:
        stu['english'] = int(english)

    stu['total'] = stu['chinese'] + stu['math'] + stu['english']
    return stu


# 删除 修改 查找都需要找学生
def search_student(stu_name, students_s):
    """
    找学生, 找到了就返回学生对象
    :param stu_name: 需要找的学生名字
    :param students_s: 学生信息列表
    :return: 找到了就返回学生对象, 没找到就返回 None --> 布尔判断结果是 False
    """
    for stu in students_s:
        if stu_name == stu['name']:
            # 找到了
            return stu


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

# 读取文件中的数据
with open('students.json', mode='r', encoding='utf-8') as f:
    students_str = f.read()

# 系统中需要用到列表对象
students = json.loads(students_str)  # 学生信息列表

while True:
    # 1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
    print(str_info)
    # 2. 用户用数字选择不同的功能(input)
    action = input('请选择您要执行的操作(请输入操作数字):')
    # print(type(action))
    # 3. 根据功能选择，执行不同的功能
    if action == '1':
        print('1. 新建学生信息')
        stu = insert_student()
        students.append(stu)
        print('##### ------------ 新建成功 ------------ #####')

    elif action == '2':
        print('2. 显示全部信息')
        print('姓名\t语文\t数学\t英语\t总分')
        for stu in students:
            print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')

    elif action == '3':
        print('3. 查询学生信息')
        name = input('请输入您要查询的学生姓名:')

        stu = search_student(name, students)
        if stu:  # 找到了
            print('姓名\t语文\t数学\t英语\t总分')
            print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
            print('##### ------------ 查询成功 ------------ #####')

        # 找完学生信息列表中的学生, 都没有找到, 就会走else代码逻辑
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '4':
        print('4. 修改学生信息')
        name = input('请输入您要修改的学生姓名:')

        stu = search_student(name, students)
        if stu:
            # 如果找到了就修改学生信息
            new_stu = insert_student()
            stu.update(new_stu)  # 更新学生字典数据

        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '5':
        print('5. 删除学生信息')
        name = input('请输入您要删除的学生姓名:')

        stu = search_student(name, students)
        if stu:
            students.remove(stu)
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '0':
        print('0. 退出系统')
        with open('students.json', mode='w', encoding='utf-8') as f:
            """将列表对象转化成字符串对象"""
            # json.dumps(需要转化的对象, 不使用默认编码)
            students_str = json.dumps(students, ensure_ascii=False)
            f.write(students_str)
            pprint.pprint(students)
        break

    else:
        print('请输入正确的操作!')

"""if ... elif ... else"""
