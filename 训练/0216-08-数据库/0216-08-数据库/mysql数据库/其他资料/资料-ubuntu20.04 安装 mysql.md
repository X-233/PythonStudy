## Ubuntu20.04 安装 MySQL

系统更新
```
sudo apt update
sudo apt upgrade
```

### MySQL安装

```
sudo apt-get install mysql-server mysql-client
```

### 查看MySQL默认用户密码

```
sudo cat /etc/mysql/debian.cnf
```

```
# Automatically generated for Debian scripts. DO NOT TOUCH!
[client]
host     = localhost
user     = debian-sys-maint
password = qGZpZvUEPkCuuXMF
socket   = /var/run/mysqld/mysqld.sock
[mysql_upgrade]
host     = localhost
user     = debian-sys-maint
password = qGZpZvUEPkCuuXMF
socket   = /var/run/mysqld/mysqld.sock
```

### 使用默认用户密码登录

```
mysql -u debian-sys-maint -p
```

### 修改root远程登录的ip为%，意思是允许所有的ip远程访问

```
use mysql;

update user set host = '%' where user = 'root' limit 1;

flush privileges;
```

### 修改root密码

```
update user set plugin='caching_sha2_password' where user='root';
```

### 打开mysql配置文件，注释3306端口于本地的绑定

```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

# bind-address = 127.0.0.1 
```

### 重启MySQL

```
systemctl status mysql.service  # 查看状态
systemctl start mysql.service  # 启动数据库
systemctl stop mysql.service  # 停止数据库
systemctl restart mysql.service  # 重启数据库
```


### MySQL安装后的目录结构分析(此结构只针对于使用apt-get install 在线安装情况)

数据库存放目录： /var/lib/mysql/

相关配置文件存放目录： /usr/share/mysql

相关命令存放目录： /usr/bin(mysqladmin mysqldump等命令)

启动脚步存放目录： /etc/rc.d/init.d/

### MySQL的卸载

```
sudo rm /var/lib/mysql/ -R
sudo rm /etc/mysql/ -R
sudo apt-get autoremove mysql* --purge
sudo apt-get remove apparmor
```

## 管理

```
systemctl status mysql
```

## 添加用户 

新建一个用户

```sql
-- 使用mysql数据库
USE mysql
 
-- 创建用户
create user 'windows'@'%' identified by 'Zhengxin...123456';

 
-- 查看用户
SELECT user, host, authentication_string FROM user WHERE USER='windows';
 
-- 修改用户密码
update user set authentication_string='' where user='windows';

ALTER USER 'windows'@'%' IDENTIFIED BY 'Zhengxin...123456';
 
-- 删除用户
DROP USER windows;
 
-- 查看权限
SHOW GRANTS FOR windows;
 
-- 授予权限
-- grant all privileges on databasename.tablename to 'user'@'host' identified by 'password';

-- 授予windows用户全局级全部权限：
-- GRANT ALL PRIVILEGES ON *.* TO 'windows'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'windows'@'%' WITH GRANT OPTION;

-- 授予windows用户针对testdb数据库全部权限：
-- GRANT ALL PRIVILEGES ON testdb.* TO 'windows';

GRANT ALL PRIVILEGES ON *.* TO 'windows';

-- 生效(刷新权限)
FLUSH PRIVILEGES;
 
-- 撤销权限
-- revoke privileges on databasename.tablename from 'username'@'host';

REVOKE ALL PRIVILEGES FROM windows;

GRANT ALL PRIVILEGES ON *.* TO 'windows2'@'%' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'windows2';
```



**GRANT命令说明：** 

+ priveleges(权限列表)，可以是 all priveleges , 表示所有权限，也可以是 select、update 等权限，多个权限的名词,相互之间用逗号分开。
+ on用来指定权限针对哪些库和表。

+ `*.* ` 中前面的 `*` 号用来指定数据库名，后面的 `*` 号用来指定表名。
  to 表示将权限赋予某个用户，@后面接限制的主机，可以是IP，IP段，域名以及%，%表示任何地方。注意：这里%有的版本不包括本地，以前碰到过给某个用户设置了%允许任何地方登录，但是在本地登录不了，这个和版本有关系，遇到这个问题再加一个localhost的用户就可以了。

+ identified by 指定用户的登录密码,该项可以省略。

+ WITH GRANT OPTION 这个选项表示该用户可以将自己拥有的权限授权给别人。注意：经常有人在创建操作用户的时候不指定 WITH GRANT OPTION 选项导致后来该用户不能使用 GRANT 命令创建用户或者给其它用户授权。

备注：可以使用GRANT重复给用户添加权限，权限叠加，比如你先给用户添加一个select权限，然后又给用户添加一个insert权限，那么该用户就同时拥有了select 和 insert 权限。

**授权原则说明：** 

权限控制主要是出于安全因素，因此需要遵循一下几个经验原则：

1. 只授予能满足需要的最小权限，防止用户干坏事。比如用户只是需要查询，那就只给select权限就可以了，不要给用户赋予update、insert或者delete权限。

2. 创建用户的时候限制用户的登录主机，一般是限制成指定IP或者内网IP段。

3. 初始化数据库的时候删除没有密码的用户。安装完数据库的时候会自动创建一些用户，这些用户默认没有密码。

4. 为每个用户设置满足密码复杂度的密码。

5. 定期清理不需要的用户。回收权限或者删除用户。