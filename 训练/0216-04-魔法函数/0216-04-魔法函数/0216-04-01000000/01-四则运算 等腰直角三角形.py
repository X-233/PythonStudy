"""
    定义一个等腰直角三角形的模型，求第三边（勾股定理：两直角边的平方和等于斜边的平方a²+b²＝c²）
    模型：Triangle
        属性：侧边（side）
        行为：
            四则运算：两个三角形面积相加，返回一个新的等腰直角三角形
            逻辑运算：两个三角形能进行面积比较
        特性：
            面积（area）
            可以给特性设置面积，然后重新求侧边
"""
import math

class Triangle:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2 / 2

    @property
    def third(self):
        return math.sqrt(self.side ** 2 + self.side ** 2)

    def __add__(self, other):
        new_area = self.area + other.area
        new_side = math.sqrt(new_area * 2)
        return Triangle(new_side)

    def __repr__(self):
        return f'<Class Triangle  {self.side}>'

t1 = Triangle(3)
t2 = Triangle(4)

t3 = t1 + t2
print(t3)


