"""
定义一个猫的外形类
"""

class Shape:
    def __init__(self):
        # 在__init__中如果属性写死了, 那么在实例化对象的时候属性都是固定的, 无法修改
        self.color = '灰色'  # 指定实例属性  颜色
        self.limbs = 4  # 指定实例属性  多少爪子
        self.behavior = ['喵喵叫']  # 指定实例属性  颜色

    def print_info(self):
        print(f'猫的颜色是: {self.color}')
        print(f'猫的脚有几只: {self.limbs}')
        print(f'猫的行为是: {self.behavior}')

cat1 = Shape()
cat1.print_info()
print('------------------------')

# cat2 = Shape('黑色', 4, ['抓人'])
# cat2.print_info()