import redis
import pymysql

redis_link = [
    # 张辉
    {'redis_key': 'zhanglin', 'redis_port': 6379, 'ip': '180.76.187.206', 'redis_name': 'default'},
]
mysql_link = [
    {'mysql_name': 'zhanglin', 'mysql_key': 'zhanglin', 'mysql_ip': '180.76.187.206', 'mysql_port': 3306,
     'mysql_database': '毕设'},
    # 毕设
]

def link_sql(my, mysql_name):
    my_1 = pymysql.connect(
        host=my[mysql_name]['mysql_ip'],
        user=my[mysql_name]['mysql_name'],
        password=my[mysql_name]['mysql_key'],
        database=my[mysql_name]['mysql_database'],
        charset='utf8mb4',
        port=my[mysql_name]['mysql_port'],
    )
    return my_1

def link_redis(red, redis_name):
    re_0 = redis.StrictRedis(
        host=red[redis_name]['ip'],
        port=red[redis_name]['redis_port'],
        password=red[redis_name]['redis_key'],
        db=0,
        username=red[redis_name]['redis_name'],
    )
    return re_0

def link(func):
    def waper(*args, **kwargs):
        links = func(*args, **kwargs)
        return links
    return waper

if __name__ == '__main__':
    redis_1 = link(link_redis)
    mysql_1 = link(link_sql)
    re_1 = redis_1(link_redis, 0)
    sql_1 = mysql_1(link_sql, 0)


