class Animal(object):
    """动物类"""
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return f'{self.name} 正在吃东西!!!'


class Tiger(Animal):
    # 如果在继承的关系下有相同的方法名, 那么会重写相关的方法
    def __init__(self, name, high, weight):
        # 首先是通过 super() 把父类属性继承过来, 后续可以拓展其他属性
        # super() 调用父类的__init__方法
        super().__init__(name, high, weight)


tiger = Tiger('虎大', '250cm', "180kg")
print(tiger.name)
print(tiger.high)
print(tiger.weight)
print(tiger.eat())
