/*
            excel(是一种格式)        sql(是一门语言)
操作软件     office excel/ wps       mysql/sql server/postgresql....
            .xlsx 文件              database 数据库
            sheet 表                table 数据表
            列                      字段
            行                      记录
*/

-- 显示数据库
show databases;

-- 创建 数据库 python 设置编码 'utf8mb4'
create database python character set 'utf8mb4';

-- 删除数据库
drop database python;


-- 选择使用的数据库
use python;

-- 显示 数据表
show tables;

-- sql 不区分大小写