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

    # 自定义比较运算符
    def __eq__(self, other):  # __eq__ == 运算符
        return self.area == other.area

    def __ge__(self, other):  # __ge__ ==
        return self.area >= other.area

    def __le__(self, other):  # __le__ ==
        return self.area <= other.area


c1 = Circle(5)
c2 = Circle(6)
print(c1.equals(c2))
# 能不能让 Circle 也支持 == 运算符
print(c1 == c2)
print(c1 >= c2, c1.__ge__(c2))
print(c1 <= c2, c1.__le__(c2))  # 比较运算符有镜像法则, 实现了大于等于,小于等于也实现了
print(1 == 2)

"""
    魔法函数可以自动调用, 也可以手动调用
    手动调用不符合人的直觉
"""
