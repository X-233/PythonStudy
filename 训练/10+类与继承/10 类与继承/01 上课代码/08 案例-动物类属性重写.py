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
    def __init__(self, name, high, weight, color):  # color 是基于继承关系, 新增的属性
        super().__init__(name, high, weight)  # 先把父类的属性继承过来
        # 老虎相比普通的动物类, 多了一个属性 -->颜色
        self.color = color  # 将新增的属性绑定到老虎类的对象上


tiger = Tiger('虎大', '250cm', '180kg', '黑白相间')
print(tiger.name)
print(tiger.high)
print(tiger.weight)
print(tiger.color)
