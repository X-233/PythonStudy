# 需求: 给定一个数字, 求 1 到这个数字之间所有数字的积
#  3 = 3 x 2 x 1
#  6 = 6 x 5 x 4 x 3 x 2 x 1

def sum_number(num):
    print(num)
    # 如果是1, 直接返回 1 的结果 --> 递归的出口
    if num == 1:
        return 1

    return num * sum_number(num - 1)


print(sum_number(5))