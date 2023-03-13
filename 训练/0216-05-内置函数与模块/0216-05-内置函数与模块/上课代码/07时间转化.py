import time

"""时间戳转结构化时间"""
now_time = time.time()
struct_time = time.localtime(now_time)  # time.localtime(时间戳)
print('时间戳转结构化时间：', struct_time)

"""结构化时间转字符串"""
str_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
print(str_time)

"""字符串时间转结构化时间"""
str_time = '2023-03-03 21:34:00'
struct_time = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
print(struct_time)

"""结构化时间转时间戳"""
print(time.mktime(struct_time))
