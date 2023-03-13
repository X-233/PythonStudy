import json  # 内置, 将Python对象和字符串之间做转化
import pprint

students = [
    {'name': '丸子', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '欧阳吹雪', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '巳月', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
]

"""在结束系统的时候会保存数据到文件"""
with open('students.json', mode='w', encoding='utf-8') as f:

    """将列表对象转化成字符串对象"""
    # json.dumps(需要转化的对象, 不使用默认编码)
    students_str = json.dumps(students, ensure_ascii=False)
    print(students_str)
    f.write(students_str)

"""在启动系统的时候会读取文件数据"""
with open('students.json', mode='r', encoding='utf-8') as f:
    students_str = f.read()

# 系统中需要用到列表对象
students = json.loads(students_str)
pprint.pprint(students)
print(type(students))
