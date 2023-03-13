show databases;
/*
    比较运算符   > < >= <= = !=(<>)
*/
-- 查询指定字段
select id, name, cate_name, brand_name, price
from goods;

-- 15.6 英寸的电脑
select id, name, cate_name, brand_name, price
from goods
where name like '%15.6%';  -- name 名字中有 15.9

-- 查找名字中包含平板电脑的产品
select id, name, cate_name, brand_name, price
from goods
where name like '%平板电脑%';