class Animal(object):
    """动物类"""
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return f'{self.name} 正在吃东西!!!'


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Tiger(Animal, Cat):
    # def __init__(self, name, high, weight):
    #     super().__init__(name, high, weight)
    pass


# tiger = Tiger('虎大', '黑白相间')
# print(tiger.name)
# print(tiger.color)

tiger = Tiger('虎大', '250cm', '180kg')
print(tiger.name)
# print(tiger.color)
print(tiger.high)
print(tiger.weight)
