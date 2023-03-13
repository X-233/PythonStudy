"""
在类中, 具有相同逻辑的方法和属性可以使用继承关系继承过来
简化代码
"""

# 师傅类
class Master(object):
    def __init__(self):
        self.secret = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')


# 徒弟类
class Apprentice(Master):
    pass
    # def __init__(self):
    #     self.secret = '[古法煎饼果子配方]'
    #
    # def make_cake(self):
    #     print(f'运用{self.secret}制作煎饼果子')


# 用实例化的徒弟类对象, 继承师傅类
wanzi = Apprentice()
print(wanzi.secret)
wanzi.make_cake()
