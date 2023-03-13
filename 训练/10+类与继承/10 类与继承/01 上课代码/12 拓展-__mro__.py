"""
炼体 PracticeBody
    属性：
        血量(blood)
        体力(power)
    行为：
        挑水（carry_water）
            挑水消耗2点体力
        砍柴（chop_wood）
            砍柴消耗3点体力

练气 PracticeMagic
    属性：
        血量
        体力
      + 灵力（magical_power）
    行为：
        挑水
            挑水消耗0.2点灵力
        砍柴
            砍柴消耗0.3点灵力
      + 御风(fly)
            御风消耗2点灵力
      + 喷火(spurt_fire)
            喷火消耗2点灵力

练神 PracticeDivine
    属性：
        血量
        体力
        灵力
      + 神力(super_power)
    行为：
      - 挑水
      - 砍柴
        御风
            御风消耗0.2点神力
        喷火
            喷火消耗0.2点神力
      + 御剑(flying_sword)
            御剑飞行消耗 2 点神力
"""

# 炼体期
class PracticeBody(object):
    def __init__(self, name, blood, power):
        self.name = name
        self.blood = blood
        self.power = power

    def carry_water(self):
        self.power -= 2

    def chop_wood(self):
        self.power -= 3

# 练气期
class PracticeMagic(PracticeBody):
    def __init__(self, name, blood, power, magical_power):
        super().__init__(name, blood, power)  # 从父类继承相同的属性
        self.magical_power = magical_power  # 新增属性

    def carry_water(self):
        self.magical_power -= 0.2

    def chop_wood(self):
        self.magical_power -= 0.3

    def fly(self):
        self.magical_power -= 2

    def spurt_fire(self):
        self.magical_power -= 2

# 练神期
class PracticeDivine(PracticeMagic):
    def __init__(self, name, blood, power, magical_power, super_power):
        super().__init__(name, blood, power, magical_power)  # 从父类继承相同的属性
        self.super_power = super_power  # 新增属性

    def carry_water(self):
        # 主动抛出一个异常
        raise Exception('炼神期不会挑水低级技能')

    def chop_wood(self):
        # 主动抛出一个异常
        raise Exception('炼神期不会砍柴低级技能')

    def fly(self):
        self.super_power -= 0.2

    def spurt_fire(self):
        self.super_power -= 0.2

    def flying_sword(self):
        self.super_power -= 2


# 多继承  多层继承
# 继承的查找顺序
# 先找自己本身 --> 再找父类的继承对象 --> ...... --> 找到基类: 如果基类找不到就报错
print(PracticeDivine.__mro__)

