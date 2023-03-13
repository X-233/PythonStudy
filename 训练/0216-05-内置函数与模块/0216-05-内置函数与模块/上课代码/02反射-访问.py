import random


class Circle(object):
    pass


class Triangle(object):
    pass


class Rect:
    pass


class_obj = random.choice([Circle, Triangle, Rect])
# print(class_obj)
self_obj = class_obj()  # 创建一个实例对象

# 分别对实例对象进行处理
# isinstance 用于判断实例对象的
if isinstance(self_obj, Circle):
    print(self_obj, '是一个圆形的实例对象')
elif isinstance(self_obj, Triangle):
    print(self_obj, '是一个三角形的实例对象')

# 只要结果是对的,都是可以的
print(issubclass(int, str))
print(issubclass(bool, int))  # bool 是 int 的子类
