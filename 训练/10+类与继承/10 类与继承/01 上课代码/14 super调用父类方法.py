# 师傅类
class Master(object):
    def __init__(self):
        self.secret = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')


# 学校类
class School(Master):
    def __init__(self):
        self.secret = '[青灯煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')
        # """方式1"""
        # # super(School, self).__init__()
        # # super(School, self).make_cake()
        #
        # """方式2"""
        # super().__init__()
        # super().make_cake()


# 徒弟类
class Apprentice(School):
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

    # 通过封装一个方法, 一次性调用所有父类同名的属性和方法
    def make_all_cake(self):
        # super() 调用父类一般是调用单继承中的父类
        # super().__init__()
        # super().make_cake()
        Master.__init__(self)
        Master.make_cake(self)

        School.__init__(self)
        School.make_cake(self)



wanzi = Apprentice()
wanzi.make_all_cake()