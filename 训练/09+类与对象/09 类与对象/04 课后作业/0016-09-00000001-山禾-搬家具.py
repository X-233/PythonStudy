"""
### 作业2

1、创建一个房子类,
+ 分别有以下属性
  名字（name）, 房子面积(area), 家具<列表>（furniture）

+ 每个房子都有添加家具的方法
    # 如果 家具占地面积 <= 房子剩余面积：可以搬入(家具列表添加家具名字数据并房子剩余面积更新：
    # 房屋剩余面积 - 该家具的占地面积 = 目前房子的面积
    # 否则：提示用户家具太大，剩余面积不足，无法容纳

2、实例化房子操作
    实例化一个房子， 面积50平米
    添加家具：（沙发，占地15平米）
    添加家具：（餐桌，占地8平米）
    添加家具：（大床，占地20平米）
    添加家具：（浴缸，占地8平米）

"""
"""请在下方编辑代码"""

class House:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.furniture = []

    def add_furniture(self, fur_name, fur_area):
        if fur_area <= self.area:
            self.area -= fur_area
            self.furniture.append(fur_name)
            print('搬入成功!')
        else:
            print('不可搬入!')

house = House('zhang', 100, [])

house.add_furniture('冰箱', 15)

