"""
作业2：
运行代码之后，请找出下面代码错误并且修正

提示：深浅拷贝
"""
import copy

data = {
    'cate': '童书馆',
    'sub_cate': None
}

sub_cate = ['科普百科', '儿童文学', '幼儿启蒙', '动漫卡通', '少儿英语']

all_cate = []

for cate in sub_cate:
    """在for循环中操作的是同一个字典对象"""
    data['sub_cate'] = cate
    # 浅拷贝: 只作用于一维数据
    # 深拷贝: 作用于各个维度数据
    all_cate.append(copy.deepcopy(data))
    # print(all_cate)

import pprint
pprint.pprint(all_cate)
