"""
假设一个班有N个学员
假设 N 为 3 ，体重分别是 180、190、200
请编写一个函数对整个班级的学员的体重求和
"""

def get_weight(stu1, stu2, stu3):
    total = stu1 + stu2 + stu3
    return total

# print(get_weight(180, 190, 200))

"""假设这个班有多少人是未知的"""
# *args  是不定长参数, 用于收集所有传进来的位置参数
# * 代表解包的意思
def get_weight_2(*args):
    print(args)
    print(type(args))
    total = 0
    for i in args:
        total += i

    return total


# print(get_weight_2(80, 90, 100, 100, 120, 130))

# **kwargs  是不定长参数, 用于收集所有传进来的关键字参数
def get_weight_3(**kwargs):
    print(kwargs)
    print(type(kwargs))
    total = 0
    for i in kwargs.values():
        total += i

    return total


print(get_weight_3(a=100, b=200, c=300))
