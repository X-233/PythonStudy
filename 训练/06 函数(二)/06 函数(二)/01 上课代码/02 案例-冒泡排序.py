
"""
需求: 任意给定一组序列数字, 比如 [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
将序列从小到大排列。
（不能使用python函数解决）

range(15)   0123456789 10 11 12 13 14
"""

def bubble_sort(arr):

    n = len(arr)  # 序列数据的长度, 用于设置比较的次数

    for i in range(n):  # 遍历序列的索引, 构建比较的次数
        for j in range(0, n - 1):  # 构建索引两两比较的范围
            if arr[j] > arr[j + 1]:  # 两两根据索引取值, 如果取出来的第一个数大于第二个数
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 就交换位置

    return arr


result = bubble_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48])
print(result)

result = bubble_sort([27, 2, 46, 4, 19, 50, 48])
print(result)

# 穷举 --> 把所有可能出现的情况全部罗列


