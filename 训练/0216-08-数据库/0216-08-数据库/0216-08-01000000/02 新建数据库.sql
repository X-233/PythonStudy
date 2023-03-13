/*
    1. 在本地数据库服务器中创建一个属于自己的数据库：python（期数-作业次数-学号）
    2. 选择数据库后创建一张 changsha 数据表，字段参考 `01 处理数据.py` 文件
    3. 将处理后的 changsha_result.csv 数据插入到数据库
*/

show databases;

use python;

show tables;

select * from bads;

drop table bads;

create table bads(
                     city varchar(255),          # 城市
                     region varchar(255),        # 行政区
                     title varchar(255),         # 门店名称
                     star_level varchar(255),    # 星级
                     star float,          # 星级得分
                     review_num float,    # 点评总数
                     mean_price varchar(20),    # 人均消费
                     comment_list1 varchar(255), # 口味
                     comment_list2 varchar(255), # 环境
                     comment_list3 varchar(255), # 环境
                     link varchar(255),          # 链接网址
                     shop_tag_cate_click varchar(255),
                     shop_tag_region_click varchar(255),
                     addr varchar(255)
);
