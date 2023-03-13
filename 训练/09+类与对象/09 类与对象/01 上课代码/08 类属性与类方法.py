class Hero:  # 类的名字叫做类对象
    """在类名下面定义的变量就叫做类属性"""
    hand = 2  # 每个英雄有两只手
    head = 1  # 每个英雄有一个头

    class_name = '人类'

    def __init__(self, name, weapon, equipment, blood):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    def attack(self, who, aggressivity):
        print(f'{self.name} 发动了攻击!  攻击了谁 --> {who.name}')
        who.blood -= aggressivity  # 谁被攻击, 那么按照攻击力减少血量
        return '攻击完成'

    @classmethod  # 标注下面这个方法是类方法, 是Python中的装饰器
    def boast(cls):  # 一般情况下类方法会调用类属性, 可以通过cls调用
        return cls.class_name + '会吹牛~'

    # 静态方法: 不需要使用类对象方法和属性, 也不需要使用实例对象方法和属性
    @staticmethod  # 标注此方法为静态方法
    def info():
        return '人类生活在地球!'


hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 100)

"""调用类属性的方式"""
# 通过实例化对象调用类属性
print(f'{hero1.name}的手有-{hero1.hand}-只手')
print(f'{hero2.name}的头有-{hero2.head}-个头')
# 通过类对象调用类属性
print(Hero.hand)
print(Hero.head)

"""修改类属性"""
# 通过实例化的对象修改类属性, 修改的值仅针对当前对象
hero1.hand = 6  # 修改hero1手的属性为 6
print(f'{hero1.name}的手有-{hero1.hand}-只手')
print(f'{hero2.name}的手有-{hero2.hand}-只手')

# 通过类对象修改类属性, 会修改所有对象的类属性
Hero.head = 3
print(f'{hero1.name}的头有-{hero1.head}-个头')
print(f'{hero2.name}的手有-{hero2.head}-个头')

"""调用类方法"""
print(hero1.boast())  # 通过实例对象调用类方法
print(Hero.boast())  # 通过类对象调用类方法

"""调用静态方法"""
print(hero1.info())  # 通过实例对象调用静态方法
print(Hero.info())  # 通过类对象调用静态方法
