-- INSERT INTO 表名(字段列表)
-- VALUES(字段值列表),(字段值列表),(字段值列表),(字段值列表);

select *
from student;


-- 插入数据
-- 字段需要一一对应
insert into student(id, name, math, chinese, english)
values (1, '张三', 60, 60, 60);


insert into student(id, name, math, chinese, english)
values (2, '李四', 60, 60, 60),
       (3, '王五', 60, 60, 60);

-- 清空数据表
truncate student;


insert into student(id, name, math, chinese, english)
values (0, '张三', 60, 60, 60),
       (0, '李四', 60, 60, 60),
       (0, '王五', 60, 60, 60);

-- 默认是插入所有字段
insert into student
values (0, '张三', 60, 60, 60),
       (0, '李四', 60, 60, 60),
       (0, '王五', 60, 60, 60);


-- 可以指定字段进行插入
insert into student(name, math, chinese)
values ('张三', 60, 60),
       ('李四', 60, 60),
       ('王五', 60, 60);

desc student;


delete
from student
where id = 20;

-- 物理删除 逻辑删除
alter table student add column is_del bool;
alter table student drop column is_del;

-- 更新字段
update student set english=100 where id=21;


-- 冗余字段
-- 地址  中国 湖南 长沙 望城区.金桥国际未来城