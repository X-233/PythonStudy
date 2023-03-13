class Dog:
    def __init__(self, name=None):
        self.name = name

    def bark(self):
        print("旺旺叫!")


class Cat:
    def __init__(self, name=None, color=None):
        self.name = name
        self.color = color

    def bark(self):
        print("喵喵叫")


dog = Dog()
cat = Cat()

arr = [dog, cat]

# 不同的对象,有一个同样的方法,在调用的时候可以当做同一个对象进行操作 -- 鸭子类型
for item in arr:
    item.bark()
