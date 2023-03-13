import redis
import pymysql

redis_link = [
    # 张辉
    {'redis_key': 'zhanglin', 'redis_port': 6379, 'ip': '180.76.187.206', 'redis_name': 'default'},
]
mysql_link = [
    {'mysql_name': 'zhanglin', 'mysql_key': 'zhanglin', 'mysql_ip': '180.76.187.206', 'mysql_port': 3306, 'mysql_database': '毕设'},
    {'mysql_name': 'windows', 'mysql_key': 'Zhengxin...123456', 'mysql_ip': '81.68.68.240', 'mysql_port': 3306, 'mysql_database': 'python'},
]

def link_sql(mysql_name):
    my_1 = pymysql.connect(
        host=mysql_link[mysql_name]['mysql_ip'],
        user=mysql_link[mysql_name]['mysql_name'],
        password=mysql_link[mysql_name]['mysql_key'],
        database=mysql_link[mysql_name]['mysql_database'],
        charset='utf8mb4',
        port=mysql_link[mysql_name]['mysql_port'],
    )
    return my_1

def link_redis(redis_name):
    re_0 = redis.StrictRedis(
        host=redis_link[redis_name]['ip'],
        port=redis_link[redis_name]['redis_port'],
        password=redis_link[redis_name]['redis_key'],
        db=0,
        username=redis_link[redis_name]['redis_name'],
    )
    return re_0

def link(func):
    def waper(*args, **kwargs):
        links = func(*args, **kwargs)
        return links
    return waper



