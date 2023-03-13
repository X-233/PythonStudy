import time

"""时间戳"""
now_time = time.time()
print('时间戳:', now_time)
print('时间戳(10):', int(now_time))
print('时间戳(13):', int(now_time * 1000))
print('时间戳(hex):', hex(int(now_time * 1000)))

"""结构化时间"""
now_time = time.localtime()
print('结构化时间:', now_time)
print('结构化时间:', now_time.tm_year)

"""字符串时间"""
print('字符串时间：', time.ctime())
print('字符串时间：', '2023-03-03 22:00:00')
