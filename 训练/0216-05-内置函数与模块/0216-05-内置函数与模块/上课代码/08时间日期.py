# datetime 封装了 time
import datetime

today = datetime.datetime.today()
print(today.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d %H:%M:%S"))

one_day = datetime.datetime.strptime('2023-03-03 22:00:00', '%Y-%m-%d %H:%M:%S')
print(one_day)
print(one_day.date())  # 获取年月日
print(one_day.time())  # 获取时分秒

today_date = today.date()  # 年月日对象
print(today_date)
today_time = today.time()  # 年月日对象
print(today_time)