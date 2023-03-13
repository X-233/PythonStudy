# 师傅类
class Master(object):
    def __init__(self):
        self.secret_shifu = '[古法煎饼果子配方]'

    def make_cake_shifu(self):
        print(f'运用{self.secret_shifu}制作煎饼果子')


# 学校类
class School(object):
    def __init__(self):
        self.secret_xuexiao = '[青灯煎饼果子配方]'

    def make_cake_xuexiao(self):
        print(f'运用{self.secret_xuexiao}制作煎饼果子')


class Apprentice(School, Master):
    # 重写父类的属性和方法, 重写需要和父类的属性或者方法名字一样
    def __init__(self):
        self.secret_1 = '[独创煎饼果子配方]'

    def make_cake_1(self):
        print(f'运用{self.secret_1}制作煎饼果子')



wanzi = Apprentice()
print(wanzi.secret_1)
wanzi.make_cake_1()

# print(wanzi.secret_shifu)
# wanzi.make_cake()

"""
在继承的基础上进行重写
    如果属性和方法的名字一样, 那么会覆盖父类的相同的属性和方法
    子类重写父类同名的属性或者方法, __init__会覆盖调所有父类的方法
"""