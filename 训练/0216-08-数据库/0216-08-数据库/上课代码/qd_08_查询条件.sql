show databases;
/*
    比较运算符   > < >= <= = !=(<>)
    逻辑运算符   AND OR NOT
    成员运算符   in not in
*/
-- 查询指定字段
select id, name, cate_name, brand_name, price
from goods;

-- 查询价格高于4000的电脑
select id, name, cate_name, brand_name, price
from goods
where price > 4000;

-- 查询价格在4000~8000的电脑
select id, name, cate_name, brand_name, price
from goods
where price > 4000
  and price < 8000;

-- 预算3000-5000，并且想买联想的电脑
select id, name, cate_name, brand_name, price
from goods
where price > 3000
  and price < 5000
  and brand_name = '联想';


-- 预算3000-5000，并且想买联想 或者是苹果的电脑
-- 预算3000-5000，并且 想买联想或者是苹果的电脑
select id, name, cate_name, brand_name, price
from goods
where price > 3000
  and price < 5000
  and (brand_name = '联想' or brand_name = '苹果');

select id, name, cate_name, brand_name, price
from goods
where price > 3000
  and price < 5000
  and brand_name in ('联想', '苹果');

