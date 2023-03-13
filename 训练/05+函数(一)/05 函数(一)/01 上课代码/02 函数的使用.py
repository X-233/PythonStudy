# # 利用函数, 求两个数的最大值
#
# def get_max(num1, num2):  # 在定义函数的时候括号内的参数叫做形式参数, 在使用的时候不具有实际意思
#     """
#     求两个数的最大值
#     :param num1: 传进来的第一个数字
#     :param num2: 传进来的第二个数字
#     :return: 返回两个数的最大值
#     """
#     max_num = 0  # 接收最大值结果
#
#     if num1 > num2:
#         max_num = num1
#
#     else:
#         max_num = num2
#
#     return max_num  # 返回结果比较的最大值
#
#
# # input()
# print(get_max(78, 75))  # 在调用函数的时候传递的参数叫做实际参数, 具有函数执行的实际意义
# print(get_max(1000.3, 10000))


def get_max(num1, num2):
    """
    求两个数的最大值
    :param num1: 传进来的第一个数字
    :param num2: 传进来的第二个数字
    :return: 返回两个数的最大值
    """

    if num1 > num2:
        return num1
    else:
        return num2


print(get_max(115, 102.5))
print(get_max(456, 789))