show databases;

use python;

show tables;

select * from bads;

drop table bads;

truncate table bads;

create table bads(
                     city varchar(255),          # 城市
                     region varchar(255),        # 行政区
                     title varchar(255),         # 门店名称
                     star_level varchar(255),    # 星级
                     star float,          # 星级得分
                     review_num int,    # 点评总数
                     mean_price varchar(20),    # 人均消费
                     comment_list1 float, # 口味
                     comment_list2 float, # 环境
                     comment_list3 float, # 环境
                     link varchar(255),          # 链接网址
                     shop_tag_cate_click varchar(255),
                     shop_tag_region_click varchar(255),
                     addr varchar(255)
);
