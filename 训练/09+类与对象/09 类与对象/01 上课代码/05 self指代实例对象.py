"""
定义一个猫的外形类
"""

class Shape:
    def __init__(self, color, limbs, behavior):
        self.color = color  # 指定实例属性  颜色
        self.limbs = limbs  # 指定实例属性  多少爪子
        self.behavior = behavior  # 指定实例属性  颜色

    def print_info(self):
        print(f'猫的颜色是: {self.color}')
        print(f'猫的脚有几只: {self.limbs}')
        print(f'猫的行为是: {self.behavior}')

    # self 指代的是实例化的一个一个的对象
    # 方法中都会使用 self 作为函数的第一个参数
    # 如果在类中函数的第一个参数是 self 那么可以叫做实例方法
    # self 的参数名字可以改, 但是不建议改, 不成文的规定
    def return_obj(self):
        # 在类的内部, 可以通过self调用属性和其他方法
        self.print_info()
        return self


cat1 = Shape('白色', 4, ['喵喵叫'])
result = cat1.return_obj()
print(id(cat1))
print(id(result))