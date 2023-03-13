import math


class Rect:  # 正方形
    def __init__(self, side):
        self.side = side

    @property  # 核心编程 面向对象 类与对象
    def area(self):
        return self.side * self.side

    def __add__(self, other):
        new_area = self.area + other.area
        new_side = math.sqrt(new_area)
        return Rect(new_side)

    def __repr__(self):
        return f'<class Rect side: {self.side:.2f}>'


class Triangle:  # 等边三角形
    def __init__(self, side):
        self.side = side

    @property  #
    def area(self):
        height = math.sqrt(self.side ** 2 - (self.side / 2) ** 2)
        return self.side * height / 2

    def __add__(self, other):
        new_area = self.area + other.area
        # 边长 = sqrt((4*面积)/sqrt(3))
        new_side = math.sqrt(new_area * 4 / math.sqrt(3))
        return Triangle(new_side)

    def __repr__(self):
        return f'<class Triangle side: {self.side:.2f}>'


rect1 = Rect(4)
triangle1 = Triangle(4)

ret1 = rect1 + triangle1  # rect1.__add__(triangle1)
ret2 = triangle1 + rect1  # triangle1.__add__(rect1)
print(ret1, ret2)
