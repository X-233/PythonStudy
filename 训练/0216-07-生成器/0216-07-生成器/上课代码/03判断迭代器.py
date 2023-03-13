from collections.abc import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))

# for item in [1, 2]:
#     print(item)

my_range = range(5)  # 可迭代对象
my_range = iter(my_range)  # 迭代器
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))  # StopIteration 获取完数据之后继续迭代就报错

for item in my_range:  # for 会自动处理 StopIteration 的异常
    print(item)
