"""
    将 changsha.csv 处理成可以给 sql 直接插入的数据，然后保存到 changsha_result.csv 文件
"""

fieldnames = ['city',  # 城市
              'region',  # 行政区
              'title',  # 门店名称
              'star_level',  # 星级
              'star',  # 星级得分
              'review_num',  # 点评总数
              'mean_price',  # 人均消费
              "comment_list1",  # 口味
              "comment_list2",  # 环境
              "comment_list3",  # 环境
              "link",  # 链接网址
              "shop_tag_cate_click",  # 分类
              "shop_tag_region_click",  # 商圈
              "addr",  # 详细地址
              ]

import pymysql

with open(r'D:\培训班\0216-08-数据库\0216-08-数据库\0216-08-01000000\changsha.csv', 'r', encoding='gbk')as f:
    list_1 = [tuple(i.split(',')) for i in f.readlines()]

print(list_1[0])

# for i in list_1:
    

