# 师傅类
class Master(object):
    def __init__(self):
        self.secret = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')


# 学校类
class School(object):
    def __init__(self):
        self.secret = '[青灯煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')


# 徒弟类
class Apprentice(School, Master):
    # 重写父类的属性和方法, 重写需要和父类的属性或者方法名字一样
    def __init__(self):
        self.secret = '[独创煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')

    # 将师傅类的方法属性重新封装在以下函数中
    def make_master_cake(self):
        Master.__init__(self)  # 取师傅类的属性
        Master.make_cake(self)  # 取师傅类的方法

    def make_school_cake(self):
        School.__init__(self)  # 取师傅类的属性
        School.make_cake(self)  # 取师傅类的方法


# 徒孙类
class Tusun(Apprentice):
    pass


zx = Tusun()
zx.make_cake()
zx.make_master_cake()
zx.make_school_cake()