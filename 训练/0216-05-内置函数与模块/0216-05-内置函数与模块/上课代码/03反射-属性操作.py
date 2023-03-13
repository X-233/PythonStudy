class Person:
    def __init__(self, name=None, age=None, bobby=None):
        self.name = name
        self.age = age
        self.bobby = bobby


person = Person()
# 全局变量
arg = 'name'
# 想用字符串给对象动态添加属性

# 给对象添加属性
# person.name = '张三'
# person.arg = '张三'  # 实例对象.实例属性(√)  实例对象.全局变量(X)

# person.name = '张三'
# setattr(person, 'name', '张三')  # 等价于 person.name = '张三'
setattr(person, arg, '张三')  # arg 指向于 'name'

# setattr(person, 'arg', 18)  # person.arg = 18

# 获取对象的属性
# print(person.name)
# print(getattr(person, 'name'))
print(getattr(person, arg))
# # 删除属性
# del person.name
# delattr(person, 'name')
delattr(person, arg)


class Student:
    def __init__(self, name=None, age=None, bobby=None):
        self.name = name
        self.age = age
        self.bobby = bobby


student = Student()
# student.score = 60


# if student.score > 60:
#     print('通过')

# 判断某一个对象没有用 score 这个属性
# if student.score:
if hasattr(student, 'score'):
    print(student.score)
else:
    print(student, '没有 score 属性')

d = {
    'name': '张三', 'age': 18, 'hobby': '干饭'
}

# 动态的操作对象的值
p = Person('王麻子')
for key, value in d.items():
    setattr(p, key, value)

# p.name = d.get('name')
# p.age = d.get('age')
# p.hobby = d.get('hobby')

print(p, p.name, p.age, p.hobby)
