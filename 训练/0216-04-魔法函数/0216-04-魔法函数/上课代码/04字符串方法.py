import math
import datetime


class Circle:
    """定义一个圆形对象"""

    def __init__(self, radius):
        self.radius = radius  # 半径

    @property
    def area(self):  # 面积
        return math.pi * self.radius ** 2

    def equals(self, other):  # 比较两个圆的面积是否相等
        return self.area == other.area

    def __eq__(self, other):  # __eq__ == 运算符
        return self.area == other.area

    def __ge__(self, other):  # __ge__ ==
        return self.area >= other.area

    def __le__(self, other):  # __le__ ==
        return self.area <= other.area

    def __add__(self, other):  # __add__
        new_area = self.area + other.area  # 面积相加
        new_radius = math.sqrt(new_area / math.pi)  # 求出新圆的半径
        return Circle(new_radius)  # 返回一个新圆对象

    def __str__(self):  # 必须返回字符串对象 输出的时候表现的内容
        return f"<class 'Circle' radius: {self.radius:.2f}>"

    def __repr__(self):  # python 调试程序的时候 显示的内容
        return f"<class 'Circle' radius: {self.radius:.2f}>"


c1 = Circle(5)
c2 = Circle(6)

c3 = c1 + c2
print(c3)
print('str', str(c3))  # str 强制转化为字符串
print([c1, c2, c3])

# today = datetime.datetime.today()
# print(today)
# print(type(today))
