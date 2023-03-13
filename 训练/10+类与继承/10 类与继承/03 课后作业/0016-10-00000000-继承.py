"""
请用面向对象的继承的方式实现以下类的封装:

    动物类（Animal）：
        属性：name, high, weight
        行为：吃

    老虎类（Tiger）：
        属性：name, high, weight
        行为：吃、老虎的狩猎技能

    狮子类（Lion）：
        属性：name, high, weight
        行为：吃、狮子的狩猎技能

    狮虎兽（Liger）：
        属性：name, high, weight
        行为：吃、既有老虎的狩猎技能、也有狮子的狩猎技能
"""


class Animal:
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        print('吃!')


class Tiger(Animal):
    def Tiger_hunt(self):
        print('老虎狩猎技能!')

class Lion(Animal):
    def Lion_hunt(self):
        print('狮子狩猎技能!')

class Liger(Tiger, Lion):
    def Liger_hunt(self):
        Tiger.Tiger_hunt(self)
        Lion.Lion_hunt(self)

lig_1 = Liger('xiaoai', 128, 200)
lig_1.Liger_hunt()
print(lig_1.high)
