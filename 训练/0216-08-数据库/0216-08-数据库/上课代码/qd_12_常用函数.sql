show databases;

select *
from goods;

-- 需要统计每一个品牌的平均价格 avg

select price, brand_name
from goods
where brand_name = '华硕';

select avg(price), brand_name
from goods
where brand_name = '苹果';

select avg(price), brand_name
from goods
;

select price, brand_name -- 几个有很多个, 品牌也有很多个
from goods
order by brand_name; -- 默认会有很多的品牌

select avg(price), brand_name -- 价格只有一个, 品牌也有很多个
from goods;


select brand_name, round(avg(price), 2) as avg_price -- 几个有很多个, 品牌也有很多个
from goods
group by brand_name
having avg_price > 4000 -- 分组之后可以过滤
order by avg_price
; -- 默认会有很多的品牌


select *
from goods;

select count(*)   as total,
       sum(price),
       avg(price) as avg_price
from goods;



select *
from goods;
