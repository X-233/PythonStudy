# datetime 封装了 time
import datetime

# 时间差对象, 可以与数字进行四则运算
one_day = datetime.timedelta(days=1)

today = datetime.datetime.today()

# 100 天之前是那一天
day1 = today - one_day * 100
print(day1)

day2 = today + one_day * 100
print(day2)

# 两个日期进行计算,得到的是时间差对象
diff = day2 - day1
print(diff)
print(diff.days)
print(diff.total_seconds())
