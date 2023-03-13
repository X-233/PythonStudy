# 需求: 给定一个数字, 求 1 到这个数字之间所有数字的和
#  3 = 3 + 2 + 1
#  6 = 6 + 5 + 4 + 3 + 2 + 1

def sum_number(num):
    print(num)
    # 如果是1, 直接返回 1 的结果 --> 递归的出口
    if num == 1:
        return 1

    return num + sum_number(num - 1)

# result = sum_number(3)
# print(result)

result = sum_number(5)
print(result)

result = sum_number(6)
print(result)

# 累计运算--> 累加  累乘