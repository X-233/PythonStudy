"""
编写一个函数，计算传入的数值序列的最大值、最小值和平均值，并一起返回，然后调用该函数
"""

# 数学思想编程
def count_array(array):
    """求最小值"""
    min_num = array[0]
    for i in array:
        if i < min_num:
            min_num = i

    """求最大值"""
    max_num = array[0]
    for i in array:
        if i > max_num:
            max_num = i

    """求平均数"""
    sum_num = 0
    for i in array:
        sum_num += i

    average_num = sum_num / len(array)

    return min_num, max_num, average_num  # 一次返回多个结果, 其类型是元组


def count_array_2(array):
    min_num = min(array)  # min(序列)  求序列中的最小值
    max_num = max(array)  # max(序列)  求序列中的最大值
    average_num = sum(array) / len(array) # sum(序列)  求序列中的和

    return min_num, max_num, average_num

print(count_array_2([10, 20, 30, 40, 50]))
print(count_array_2([10, 20, 30, 40, 50, 60, 70]))