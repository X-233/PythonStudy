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
class Home:
    def __init__(self, name, area):
        self.name = name  # 房子名字
        self.area = area  # 房子面积
        self.free_area = area  # 使用传进来的房子面积, 默认最为房子的剩余面积
        self.furniture = []  # 房子家具列表

    def add_furniture(self, item):  # [家具名字, 占地面积]
        # 如果 家具占地面积 <= 房子剩余面积：可以搬入(家具列表添加家具名字数据并房子剩余面积更新：
        # 房屋剩余面积 - 该家具的占地面积 = 目前房子的面积
        # 否则：提示用户家具太大，剩余面积不足，无法容纳
        if item[1] <= self.free_area:
            self.furniture.append(item)
            print(f'{item[0]} 添加成功!!!')
            self.free_area -= item[1]
        else:
            print('家具太大，剩余面积不足，无法容纳!!')


fz = Home('恒大地产', 50)
fz.add_furniture(['沙发', 15])
fz.add_furniture(['餐桌', 8])
fz.add_furniture(['大床', 20])
fz.add_furniture(['浴缸', 8])
print(fz.free_area)

