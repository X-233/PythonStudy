show databases;

-- 查询指定字段
select id, name, cate_name, brand_name, price
from goods;


-- 查询价格在4000~8000的电脑
select id, name, cate_name, brand_name, price
from goods
where price > 4000
  and price < 8000
order by price desc;
-- order by 字段 根据某一个字段进行排序
-- 排序的方式 desc 降序 从高到低
-- 排序的方式 asc 升序(默认) 从低到高

select id, name, cate_name, brand_name, price
from goods
where price > 4000
  and price < 8000
order by cate_name, brand_name;

select id, name, cate_name, brand_name, price
from goods
where price > 4000
  and price < 8000
order by brand_name, cate_name;