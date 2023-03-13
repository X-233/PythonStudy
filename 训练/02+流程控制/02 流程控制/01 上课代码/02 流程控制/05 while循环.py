"""打印5遍 我喜欢 python"""
# print('我喜欢 python')
# print('我喜欢 python')
# print('我喜欢 python')
# print('我喜欢 python')
# print('我喜欢 python')

"""
while 成立条件(最终返回一个布尔类型):  # 如果这个条件一直成立, 就会出现死循环
    循环里面重复执行的代码
"""

# while True:
#     print('我喜欢 python')


# 通过控制循环条件, 来限制 while 的循环次数
i = 0   # 0 1 2 3 4
while i < 5:
    print('我喜欢 python')
    i += 1  # 每一次执行循环任务, 就把i值加1  等价于 i=i+1