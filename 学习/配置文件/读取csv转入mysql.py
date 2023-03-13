import pymysql

# conn_1 = pymysql.connect(host='180.76.187.206', port=3306, user='zhanglin', passwd='zhanglin', db='毕设', charset='utf8mb4')
conn = pymysql.connect(host='81.68.68.240', port=3306, user='windows', passwd='Zhengxin...123456', db='python', charset='utf8mb4')
cursor = conn.cursor()


with open(r'D:\培训班\0216-08-数据库\0216-08-数据库\0216-08-01000000\changsha.csv', 'r', encoding='gbk')as f:
    list_1 = [tuple(i.split(',')) for i in f.readlines()]

list_2 = list_1[0]


f = open(r'changsha.sql', 'w', encoding='utf-8')
n = 0
for i in list_1:
    insert = "insert into bads values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    try:
        cursor.execute(insert, i)
        n += 1
        if n % 100 == 0:
            conn.commit()
            print("Success!")
    except Exception as e:
        conn.rollback()
        print(e)
cursor.close()
f.close()

