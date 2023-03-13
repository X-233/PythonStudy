"""
创建一个游戏英雄类，

分别有以下属性
    名字（name），武器（weapon），装备（equipment），血量（blood）

每个英雄类都有游戏技能，分别为（行为）
  攻击（attack）, 对被攻击人造成对等的攻击力伤害

创建两个英雄
    '黄忠', '弓箭', ['头盔', '靴子'], 100
    '刘备', '剑', ['头盔', '盔甲'], 100
"""
class Hero:
    def __init__(self, name, weapon, equipment, blood):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    def attack(self, who, aggressivity):
        """
        攻击方法, 对被攻击人造成对等的攻击力伤害, 比如你的攻击力是多少那么被攻击人生命值就减少多少
        :param who: 传入需要攻击的对象, 传入一个实例化的对象
        :param aggressivity: 本次攻击的攻击力
        :return:
        """
        print(f'{self.name} 发动了攻击!  攻击了谁 --> {who.name}')
        who.blood -= aggressivity  # 谁被攻击, 那么按照攻击力减少血量
        return '攻击完成'


hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 100)

print('被攻击前的血量', hero2.blood)
# 在调用的方法的时候, 可以设置参数, 将对象传递到调用的方法中
hero1.attack(hero2, 10)

print('被攻击后的血量', hero2.blood)