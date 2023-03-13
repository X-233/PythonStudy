import math


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


c1 = Circle(5)
c2 = Circle(6)

# 两个球面积相加,得到一个新的球
# new_area = c1.area + c2.area
# new_radius = math.sqrt(new_area / math.pi)
# print(new_radius)
# c3 = Circle(new_radius)
# print(c3, c3.area, c2.area + c1.area)

c3 = c1 + c2
print(c3, c3.area, c2.area + c1.area)

print((c3 + c2 + c1).radius)  # 封装直接直接把圆对象当做 int 对象进行加减乘除的元素 计算的是面积

temp = c3 + c2
temp = temp + c1
print(temp.radius)

# new_arr = [1, 2, 3] + [4, 5, 6]
# new_str = '123' + '456'

c4 = Circle(3)
c5 = Circle(4)

print(c5.radius)
c5 += c4  # __add__ __iadd__
print(c5.radius)
"""可以更好的将现实生活照的事务抽象为对象
"""
