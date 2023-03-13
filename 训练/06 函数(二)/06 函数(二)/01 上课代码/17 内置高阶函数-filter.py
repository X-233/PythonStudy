list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 需要满足lambda的条件
# result = filter(lambda x:x % 2 == 0, list1)
result = filter(lambda x:x % 2 != 0, list1)
print(result)
print(list(result))