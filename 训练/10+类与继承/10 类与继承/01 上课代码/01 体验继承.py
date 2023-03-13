# object 类, 在python中是所有类的基类
# A(object)  定义了一个A类, 继承自object
# 如果继承自基类, 那么可以省略
class A(object):  # 在类中 () 表示类的继承关系, 不代表参数
    def __init__(self):
        self.num = 100
        self.score = 56

    def print_info(self):
        print(self.num)


# 定义了一个B类, 继承自A类
# 子承父业:  B类继承自A类, 会继承到A类的所有方法和属性
class B(A):
    pass


obj1 = B()
print(obj1.num)  # 如果子类继承自父类, 那么会继承父类所有的属性
print(obj1.score)  # 如果子类继承自父类, 那么会继承父类所有的属性

obj1.print_info()  # 如果子类继承自父类, 那么会继承父类所有的方法

