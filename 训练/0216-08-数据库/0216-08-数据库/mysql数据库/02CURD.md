create(新增) update(更新) read(读取) delete(删除)

## 新增数据

### 插入  

> INSERT INTO

语法1 - 【常用；支持多行；可用于子查询】

```sql
INSERT INTO 表名(字段列表)
VALUES(字段值列表),(字段值列表),(字段值列表),(字段值列表);
```

注意

- 如果想设置空值，可以用NULL表示
- 字段列表和字段值列表必须一一对应
- 字段列表的顺序可以和表定义顺序不同
- 可以省略某些字段

### 更新

> UPDATE 

```sql
UPDATE 表名 SET 字段名=值,字段名=值
WHERE 筛选条件;
```

### 删除

> DELETE FROM

单表删除

```sql
DELETE FROM 表名
WHERE 筛选条件;
```

### 清空

> TRUNCATE TABLE

- 语法

  ```sql
  TRUNCATE TABLE boys;
  ```
  
- 注意事项

  - DELETE FROM 是删除表中某些行数据，TRUNCATE TABLE 是清空整张表
  - DELETE FROM 删除后，自增字段不重置；TRUNCATE TABLE 清空后，自增字段重置为1
  - DELETE FROM 可以回滚，TRUNCATE TABLE 不能回滚

刚才我们新建了两张表，使用语句 `SELECT * FROM employee;` 查看表中的内容，可以看到 employee 表中现在还是空的：

```sql
mysql> SELECT * FROM employee;
Empty set (0.00 sec)

mysql> 
```

我们通过 INSERT 语句向表中插入数据，语句格式为：

```sql
INSERT INTO 表的名字(列名a,列名b,列名c) VALUES(值1,值2,值3);
```

我们尝试向 employee 中加入 Tom、Jack 和 Rose：

```sql
INSERT INTO employee(id,name,phone) VALUES(01,'Tom',110110110);

INSERT INTO employee VALUES(02,'Jack',119119119);

INSERT INTO employee(id,name) VALUES(03,'Rose');
```

你已经注意到了，有的数据需要用单引号括起来，比如 Tom、Jack、Rose 的名字，这是由于它们的数据类型是 CHAR 型。此外 **VARCHAR,TEXT,DATE,TIME,ENUM** 等类型的数据也需要单引号修饰，而 **INT,FLOAT,DOUBLE** 等则不需要。

第一条语句比第二条语句多了一部分：`(id,name,phone)` 这个括号里列出的，是将要添加的数据 `(01,'Tom',110110110)` 其中每个值在表中对应的列。而第三条语句只添加了 `(id,name)` 两列的数据，**所以在表中Rose的phone为NULL**。

现在我们再次使用语句 `SELECT * FROM employee;` 查看 employee 表，可见 Tom 和 Jack 的相关数据已经保存在其中了：

```
mysql> SELECT * FROM employee;
+------+------+-----------+
| id   | name | phone     |
+------+------+-----------+
|    1 | Tom  | 110110110 |
|    2 | Jack | 119119119 |
|    3 | Rose |      NULL |
+------+------+-----------+
3 rows in set (0.00 sec)
```



## 查询

> Data Query Language[DQL]

SQL 中最常用的 SELECT 语句，用来在表中选取数据，本节实验中将通过一系列的动手操作详细学习 SELECT 语句的用法。

**练习用数据库导入**

- 下载相关资源中的 `select.sql`
- 执行 sql 脚本

```sql
source myemployees.sql;
```

### 基础查询

#### SELECT子句

```sql
SELECT 查询字段 FROM 表名;

-- 查询字段包括：表的字段，常量值，表达式，函数
-- 查询的结果是一个虚拟的表
```

- 查询表中单个字段

  ```sql
  SELECT name FROM employees;
  ```
  
- 查询表中多个字段

  ```sql
  SELECT name, salary, age FROM employees;
  ```
  
- 查询表中所有字段

  ```sql
  SELECT * FROM employees;
  ```

#### 字段起别名

```sql
方式一：SELECT name AS 姓 FROM employees;
方式二：SELECT name 姓 FROM employees;

特殊符号：SELECT last_name AS "OUT#PUT" FROM employees;
```

#### 查询结果去重

```sql
SELECT DISTINCT department_id FROM employees;
```



### 条件查询

#### WHERE子句

```sql
SELECT 查询列表 
FROM 表名
WHERE 条件表达式;
```

#### 比较运算符

```sql
> < >= <= = !=(<>) 
```

#### 逻辑运算符

```sql
&&  ||  !
AND OR NOT
```


#### 模糊查询

##### 模糊查询关键字

| 模糊查询语句      | 注意事项                                                     |
| ----------------- | ------------------------------------------------------------ |
| LIKE              | 与通配符配合使用                                             |
| BETWEEN  x  AND y | 包含边界，等价于 >= x && <= y                                |
| IN                | IN ( 待选列表 )，待选列表中的元素类型要相同                  |
| IS NULL           | 不能用 = 判断是否是 NULL，只能用 IS 判断是否是 NULL，仅可以判断 NULL |

###### 通配符

```sql
% ：任意多个字符，包含0个
_ ：任意1个字符
```

##### 转义通配符

```sql
\_
\%
```



### 排序查询

#### ORDER BY 子句

```sql
SELECT *
FROM employees
ORDER BY salary DESC; -- DESC：降序，ASC:升序，默认为 ASC
```

#### 多重排序标准

```sql
-- 先按 salary 进行升序排序，保证满足前提条件的情况下，按 employee_id 进行降序排序
SELECT *
FROM employees
ORDER BY salary ASC, employee_id DESC;
```



### 分组查询

#### GROUP BY 子句

```sql
SELECT
FROM
WHERE
GROUP BY 
ORDER BY
```

#### HAVING （过滤）子句

```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```


### 常用函数

#### 数学函数

- SUM：忽略 NULL
- AVG：忽略 NULL
- MAX：忽略 NULL
- MIN：忽略 NULL
- COUNT：忽略 NULL
- 注意事项
  - sum avg 可以处理数值
  - max，min，count可以处理任何类型
  - 分组函数都忽略 NULL
  - 可以和 distinct 配合实现去重
  - COUNT(*) ：统计行数，只要有不含 NULL 的，都算一行
  - COUNT(1)：统计行数，只要有不含 NULL 的，都算一行 
  - 和分组函数一同查询的字段要求是 group by 后的字段

- ROUND
```sql
SELECT ROUND(4.56); // 5
SELECT ROUND(-1.56) // -2
SELECT ROUND(-1.567, 2) // -1.57 
```

- CELL
```sql
SELECT CELL(1.0001) // 2
SELECT CELL(-1.02)  // -1
SELECT CELL(1.00)   // 1
```

- FLOOR
```sql
SELECT FLOOR(1.0001) // 1
SELECT FLOOR(-9.8)   //-10
```

- TRUNCATE
```sql
SELECT TRUNCATE(1.699999,1);  // 1.6
```

#### 日期函数

- NOW
```sql
SELECT NOW();
```

- CURDATE
```sql
SELECT CURDATE();
```

- CURTIME
```sql
SELECT CURTIME();
```

- YEAR
```sql
SELECT YEAR(NOW());
SELECT YEAR("2018-9-14 08:23:57");
```

> MONTH，DAY，HOUR，MINUTE，SECOND 同上

- STR_TO_DATE
```sql
STR_TO_DATE("9-13-1999", "%m-%-%y")

%y 18 %Y 2018
%m 08 %c 8
%d 08
%H 24小时制
%h 12小时制
%i 35
%s 05
```

- DATE_FORMAT
```sql
DATE_FORMAT("2018/6/6","%Y年%m月%d日")
```
