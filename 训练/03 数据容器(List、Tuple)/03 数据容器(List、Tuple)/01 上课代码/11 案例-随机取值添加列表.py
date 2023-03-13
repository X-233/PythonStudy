"""
随机取10次 1 到 10 范围内的整数数据, 添加到列表
"""
# import 模块名
"""
内置模块: 在安装解释器自带的模块, 不需要额外安装
第三方模块: 基于Python开源的特性, 团队自己写的模块, 受官方认证的, 需要咱们自己安装 pip install +模块名
"""

import random  # 随机数模块 , 内置模块

# print(random.randint(1, 10))  # 1是起始值, 3是结束之, 闭区间

result_list = []

for i in range(10):
    result_list.append(random.randint(1, 10))

print(result_list)

