"""
把列表中所有人都变成sb,比方: Tencent_sb
"""
name = ['Tencent', 'Zhihu', 'Baidu']

"""请在下方编辑代码"""

# 递归函数   匿名函数   内置函数<map  zip(组包函数)  filter  reduce>
def func(x):
    return x + '_sb'  # return 返回值就是序列中每一个数据最终映射的结果

# map函数中第一个参数, 指定一个函数名, 不是指定调用函数的结果
# map 函数中会把序列数据中每一个数据都传入到指定的函数
# map 会根据指定函数进行序列的映射
result = map(func, name)
print(result)
print(list(result))
