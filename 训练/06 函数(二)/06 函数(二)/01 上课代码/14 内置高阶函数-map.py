

list1 = [1, 2, 3, 4, 5]

# 求序列数据中数据的平方
def func(x):
    return x ** 2

# map(映射函数对象, 需要映射的序列数据)
# result = map(func, list1)
result = map(lambda x:x ** 2, list1)
print(result)  # 返回的是一个map对象 <map object at 0x000001DF8279A190>
print(list(result))
