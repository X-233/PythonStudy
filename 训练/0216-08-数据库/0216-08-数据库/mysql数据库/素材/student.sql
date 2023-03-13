show databases;

use python;

create table teachers
(
    id      int primary key auto_increment,
    name    varchar(10) not null,
    subject varchar(10),
    level   int
);
insert into teachers(id, name, subject, level)
values ("1", "杨丽华", "语文", "1"),
       ("2", "唐艳", "语文", "1"),
       ("3", "徐文", "语文", "1"),
       ("4", "赵玉华", "数学", "1"),
       ("5", "李丹丹", "数学", "1"),
       ("6", "张桂荣", "数学", "1"),
       ("7", "都浩", "英语", "1"),
       ("8", "王玲", "英语", "1"),
       ("9", "王云", "英语", "1");

create table class
(
    id      int primary key auto_increment,
    name    varchar(10) not null,
    total   int,
    chinese int,
    math    int,
    english int,
    constraint t_chinese foreign key (chinese) references teachers (id),
    constraint t_math foreign key (math) references teachers (id),
    constraint t_english foreign key (english) references teachers (id)
);
insert into class(id, name, total, chinese, math, english)
values ("1", "一班", "50", "1", "4", "7"),
       ("2", "二班", "40", "2", "5", "8"),
       ("3", "三班", "48", "3", "6", "9");

drop table students;
create table students
(
    id     int primary key auto_increment,
    name   varchar(10) not null,
    class  int,
    gender varchar(2),
    constraint v_class foreign key (class) references class (id)
);
insert into students(id, name, class, gender)
values ("1", "段凤兰", "1", "女"),
       ("2", "成霞", "1", "女"),
       ("3", "张建", "1", "男"),
       ("4", "江秀梅", "2", "女"),
       ("5", "林萍", "2", "女"),
       ("6", "郑勇", "2", "男"),
       ("7", "黄凯", "3", "男"),
       ("8", "罗瑜", "3", "男"),
       ("9", "刘东", "3", "男");


create table recodes(
    id int primary key auto_increment,
    times int,
    student int,
    math int,
    chinese int,
    english int,
    constraint v_stu foreign key (student) references students (id)
);
insert into recodes(id, times, student, math, chinese, english)
values ("1", "1", "1", "65", "66", "67"),
       ("2", "1", "2", "66", "67", "68"),
       ("3", "1", "3", "67", "68", "69"),
       ("4", "1", "4", "68", "69", "70"),
       ("5", "1", "5", "69", "70", "71"),
       ("6", "1", "6", "70", "71", "72"),
       ("7", "1", "7", "71", "72", "73"),
       ("8", "1", "8", "72", "73", "74"),
       ("9", "1", "9", "73", "74", "75")
;