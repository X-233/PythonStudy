"""面向过程创建一个对象"""
# stu1 = {'name': '小明', 'score': 90}
# stu2 = {'name': '正心', 'score': 59}
#
# def print_score(student):
#     print(f'姓名: {student["name"]}, 成绩: {student["score"]}')
#
# print_score(stu1)
# print_score(stu2)


"""
如果按照规则<属性 方法>进行划分, 我们可以把具有相同属性和方法的对象聚合成一个类
类可以把每一个对象, 通过类这个模板抽象<创建>出来
"""

# 将所有的对象创建一个模板<类>
# class 是声明一个类的关键字, Student 是类的名字 --> 要用大驼峰命名法
class Student:
    """
    类有属性: 实例属性, 类属性, 用来描述对象
    类有方法: 一般类里面的方法是提供给对象做的行为
    """
    # __init__ 是一个在class类中具有特殊功能的函数
    # 叫做初始化函数, 作用: 给对象进行属性设置的, 指的是实例属性, 构造函数
    # 在通过类创建对象的时候, 这个函数会默认的被执行, 在创建对象最开始的时候执行
    def __init__(self, name, score):
        self.name = name  # 属性绑定到对象上
        self.score = score  # 属性绑定到对象上

    # 对象方法1
    # 在类当中可以通过 self 可以在类的任意地方调用属性和方法,
    def print_info(self):
        print(f'姓名: {self.name}, 成绩: {self.score}')
        return 100

    def eat(self):
        print(f'{self.name} 正在吃饭!')

"""调用属性和方法"""
# 1. 实例化对象, 方式: 类的名字+()  --> 根据类这个模板实例化对象
person1 = Student('丸子', 90)
# print(person1)

# 2.实例化对象以后可以调用对象的方法和属性
"""调用方法"""
print(person1.print_info())
person1.eat()

"""调用对象的实例属性"""
print(person1.name)
print(person1.score)

"""可以通过类这个模板实例化很多对象"""
person2 = Student('正心', 59)
person2.print_info()

person3 = Student('自游', 89)
person3.print_info()
