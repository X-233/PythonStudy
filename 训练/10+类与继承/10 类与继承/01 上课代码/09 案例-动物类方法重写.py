class Animal(object):
    """动物类"""
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return f'{self.name} 正在吃东西!!!'


class Tiger(Animal):
    """老虎类"""
    def __init__(self, name, high, weight, color):
        super().__init__(name, high, weight)
        self.color = color

    # def eat(self):
    #     # 子类中相同的方法会覆盖父类中相同方法的结果
    #     return f'{self.name} 正在咔咔咔的吃东西'

    def eat(self):
        # 子类中相同的方法会覆盖父类中相同方法的结果
        # 基于父类的函数功能拓展
        return super().eat() + '发出咔咔咔的声音'


tiger = Tiger('虎大', '250cm', '180kg', '黑白相间')
print(tiger.name)
print(tiger.high)
print(tiger.weight)
print(tiger.color)
print(tiger.eat())
