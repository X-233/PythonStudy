show tables;


-- 创建数据表
create table student
(
    id      int primary key auto_increment, -- 主键
    name    varchar(255),                   -- 姓名字段
    math    float,
    chinese float,
    english float
);

-- 查看数据表的结构
desc student;

-- 新增一列
-- ALTER TABLE 表名字 ADD COLUMN 列名字 数据类型 约束;
alter table student add column total float;

-- 删除一列
alter table student drop column total;

select * from student;
