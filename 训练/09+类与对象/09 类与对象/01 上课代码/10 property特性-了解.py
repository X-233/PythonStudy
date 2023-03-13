class Triangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    # 这个方法在调用的时候没参数, 可以把方法在调用的时候转化成属性调用
    @property
    def area(self):
        return self.w * self.h / 2


t = Triangle(3, 4)
# print(t.area())
print(t.area)

"""
类与对象的概念

类的属性和方法
    属性: 实例属性, 类属性
    方法: 实例方法, 类方法, 静态方法

类的特性, 对象的特性
"""