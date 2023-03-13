show databases;

select * -- * 通配符
from goods;

-- 查询指定字段
select id, name, cate_name, brand_name, price
from goods;

-- 查询一个字段
select name
from goods;

-- 查询之后给字段起别名 as
select id, name as name_2
from goods;

-- 对查询的结果去重
select id, brand_name
from goods;


select brand_name
from goods;

-- 对查询出来的结果进行去重
select distinct brand_name, id
from goods;