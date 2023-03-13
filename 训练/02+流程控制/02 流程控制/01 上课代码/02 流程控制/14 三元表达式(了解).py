# a = int(input("请输入a："))
# b = int(input("请输入b："))
# max_number = 0
#
# if a > b:
#     max_number = a
# else:
#     max_number = b
#
# print(max_number)

"""三元表达式"""

a = int(input("请输入a："))
b = int(input("请输入b："))

# 结果1 if 条件 else 结果2
# 满足条件返回左边的结果1, 不满足条件返回右边的结果2
# 只能判断两种情况, 以及只能针对比较简单的表达式判断
max_number = a if a > b else b
print(max_number)

# 代码的可读性不高