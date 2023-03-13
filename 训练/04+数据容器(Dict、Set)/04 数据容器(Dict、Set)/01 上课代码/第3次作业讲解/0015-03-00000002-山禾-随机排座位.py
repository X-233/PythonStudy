# -*- coding: utf-8 -*-
"""
作业1：
有 N 个人要参加会议，现在需要随机安排座位。
请用 python实现将N个人随机安排座位

提示：
    可以导入随机函数模块 random
    random.randint(a, b)
    Return random integer in range [a, b], including both end points.
    在 [a, b] 之间返回一个随机整数，包括 a, b 本身。
"""
import random

name = """
邓永明    廖德超    张勇 杨久林    戴贵富    秦代坤    李元东 田显余
"""
# 有多少个人
name_list = name.split()

site_list = ['1号办公室1位置', '1号办公室2位置', '1号办公室3位置',
             '2号办公室1位置', '2号办公室2位置', '2号办公室3位置',
             '3号办公室1位置', '3号办公室2位置']

# 答案放这里
seating = []
# 答案以二维列表输出 [('1号办公室1位置', '秦代坤'), ('1号办公室2位置', '廖德超'),.......]
"""自己在下方编写代码实现功能"""

# 随机安排位置: 人<人随机> 位置<位置随机>
for index in range(len(site_list)):
    # # 为什么名字会重复? 不清楚的敲 2, 清楚的敲 1
    # # len(site_list) == 8 固定不变
    # # random.randint(0, 7)  --> [0,1,2,3,4,5,6,7]
    # name_index = random.randint(0, len(site_list) - 1)  # 随机取人名的时候不能重复
    # # 顺序进行排位置
    # name = name_list[name_index]

    # len(name_list) == 8
    # random.randint(0, len(name_list) - 1)  # 每次生成的随机值范围都会发生变化
    name_index = random.randint(0, len(name_list) - 1)
    name = name_list.pop(name_index)  # 每一次获取名字的时候, 都会修改原来的列表

    site = site_list[index]
    seating.append([site, name])

print(seating)
