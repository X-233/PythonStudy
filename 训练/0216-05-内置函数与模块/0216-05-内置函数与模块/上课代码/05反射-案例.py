import pprint

arg, bb, cc, dd, ee, ff, gg = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
names = [arg, bb, cc, dd, ee, ff, gg]

print(names)
# 用遍历的字符串构建字典
print(arg, str(arg))

pprint.pprint(globals())
globals_back = globals().copy()  # 复制一份全局变量
value_key = {}
for key, value in globals_back.items():
    value_key[id(value)] = key
print(value_key)

data_dict = {}
for i in names:
    print(id(i))
    print(value_key[id(i)])
    data_dict[value_key[id(i)]] = i
print(data_dict)
# # 需要动态生成下面的内容
# my_dict = {
#     'aa': 'a',
#     'bb': 'b',
#     'cc': 'c',
#     'dd': 'd',
#     'ee': 'e',
#     'ff': 'f',
#     'gg': 'g',
# }
