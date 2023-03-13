"""
球球大作战

球的属性
    半径
    周长
    面积

需要实现的行为：
    大球吃小球，面积相加，返回一个新的球


r 为班级，D 为直径
面积：S=πr²; S=π(d/2）^2
周长：C=πD=2πR
"""
import math

print(math.pi)


class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return math.pi * self.r ** 2

    @property
    def c(self):
        return math.pi * self.r * 2

    def __add__(self, other):
        new_area = self.area + other.area
        new_r = math.sqrt(new_area / math.pi)
        self.r = new_r  # 修改原来的对象
        return Circle(new_r)

    def __gt__(self, other):
        return self.area > other.area

    def __repr__(self):
        return f"<Circle({self.r})>"


c1 = Circle(3)
c2 = Circle(4)
print(c1, c2)
if c1 > c2:
    # c1 = c1 + c2
    c1 + c2
else:
    # c2 = c2 + c1
    c2 + c1
print(c1, c2)
