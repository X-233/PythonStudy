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
# 操作都是同一个字典, 追加到列表,如果字典改变, 列表里面的数据也会发生变化
for cate in sub_cate:
    data['sub_cate'] = cate
    all_cate.append(copy.copy(data))


print(all_cate)
