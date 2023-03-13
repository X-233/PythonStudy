"""
定义一个猫的外形类
"""

class Shape:
    # 在初始化方法中, 设置参数, 那么在实例化对象的时候就要根据位置传递参数才能实例化对象
    def __init__(self, color, limbs, behavior):
        self.color = color  # 指定实例属性  颜色
        self.limbs = limbs  # 指定实例属性  多少爪子
        self.behavior = behavior  # 指定实例属性  颜色

    def print_info(self):
        print(f'猫的颜色是: {self.color}')
        print(f'猫的脚有几只: {self.limbs}')
        print(f'猫的行为是: {self.behavior}')

cat1 = Shape('白色', 4, ['喵喵叫'])
cat1.print_info()
print('------------------------')

cat2 = Shape('黑色', 4, ['抓人', '喵喵叫', '铲屎'])
cat2.print_info()