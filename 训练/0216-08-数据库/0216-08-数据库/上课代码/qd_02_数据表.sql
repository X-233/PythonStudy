show tables;

/*
CREATE TABLE 表名 (
    字段名 字段类型【(长度)】【约束】,
    字段名 字段类型【(长度)】【约束】,
    ...
    字段名 字段类型【(长度)】【约束】,
    字段名 字段类型【(长度)】【约束】
);
*/
-- 创建数据表
create table student
(
    id      int primary key auto_increment, -- 主键
    name    varchar(255),                   -- 姓名字段
    math    float,
    chinese float,
    english float
);

desc student;


/*
    char            固定长度的字符串(手机号/身份证号)
    varchar         可以改变长度的字符串(QQ)

    qq 号长度在 5-11 的范围
    varchar(11)     根据QQ的实际长度占用空间
    char(11)        固定长度 11

    mobile 手机号 固定11位的长度
    char(11)        11位存储空间,开销相比 varchar 更小
    varchar(11)     11位存储空间
*/


-- DROP TABLE IF EXISTS 表名;
drop table student;
-- 如果数据表存在就删除
drop table if exists student;