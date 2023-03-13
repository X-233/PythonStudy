# 师傅类
class Master(object):
    def __init__(self):
        self.secret = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')


# 学校类
class School(object):
    def __init__(self):
        self.secret_1 = '[青灯煎饼果子配方]'

    def make_cake_1(self):
        print(f'运用{self.secret_1}制作煎饼果子')


# 徒弟类, 继承自多个类
# 如果一个类继承多个父类, 那么相同的属性和方法在调用的时候会遵循就近原则
# 在多继承关系中, 会优先继承第一个父类同名的属性和方法
class Apprentice(School, Master):
    pass


# 用实例化的徒弟类对象, 继承师傅类
wanzi = Apprentice()
print(wanzi.secret_1)
wanzi.make_cake()
