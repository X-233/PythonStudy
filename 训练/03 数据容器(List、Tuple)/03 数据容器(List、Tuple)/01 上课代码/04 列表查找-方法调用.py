name_list = [4, 2, 1, 2, 0, 6, 2, '2', ' ', ' ', ' ']

"""知道一个元素在列表里面, 现在想知道这个元素在列表中的位置"""
# index 指定数据查找列表中该数据第一次出现的索引位置
# print(name_list(2))  # 查找2在列表中的索引位置, 只会找第一次出现的数据索引
# print(name_list.index(10000))  # 如果元素在列表中不存在就会报错

"""列表中有重复的数据，要统计某个重复的数据出现的次数"""
print(name_list.count(2))  # 2在列表中出现了多少次
print(name_list.count(4))  # 4在列表中出现了多少次

# print(name_list.index())

"""想知道列表中数据量有多少？"""
print(len(name_list))  # 是数据个数<从1开始>, 不是索引<从0开始>


"""判断某个数据在不在列表里面"""
print(0 in name_list)
print(0 not in name_list)

