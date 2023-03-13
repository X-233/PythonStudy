import pprint


# import pygame
# from pygame import *
# import json
# del json
def file():
    filename = 'pygame'
    age = 18
    print(globals())
    print(locals())  # 打印局部环境的变量


class Person:
    def __init__(self, name=None, age=None, bobby=None):
        self.name = name
        self.age = age
        self.bobby = bobby
        print(globals())
        print(locals())

    def show(self):
        print(globals())
        print(locals())


pprint.pprint(globals())  # 获取当前所有的全局变量 是一个字典
file()
Person()
Person().show()


class Person:
    name = "John"
    age = 36
    country = "norway"


x = vars(Person)
print([item for item in x.items() if not item[0].startswith('__')])
