"""
有N个人要参加会议，现在需要安排座位。
请用python实现将N个人安排座位
"""
# 员工
name = """
邓永明    廖德超    张勇 杨久林    戴贵富    秦代坤    李元东 田显余
"""
# 办公室名字
site_list = ['1号办公室1位置', '1号办公室2位置', '1号办公室3位置',
             '2号办公室1位置', '2号办公室2位置', '2号办公室3位置',
             '3号办公室1位置', '3号办公室2位置']

# 答案以二维列表输出 [['1号办公室1位置', '秦代坤'], ['1号办公室2位置', '廖德超'],.......]
"""自己在下方编写代码实现功能"""

name_list = name.split()
# print(name_list)

result_list = []  # 存放结果的列表

for i in range(len(name_list)):
    result_list.append([name_list[i], site_list[i]])

# print(result_list)

import pprint  # 格式化输出模块, 内置
pprint.pprint(result_list)