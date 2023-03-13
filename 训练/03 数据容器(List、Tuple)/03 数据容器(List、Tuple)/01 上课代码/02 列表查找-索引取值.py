"""列表是有序的数据容器"""
name_list = ['正心', '丸子', '自游', '巳月', '秦淮', '木子']

# 列表中的顺序位置, 是从0开始的
# 索引位置/下标
print(name_list[1])
print(name_list[0])
# print(name_list[100])  # 如果根据索引取值超过了列表的范围就会报错: IndexError: list index out of range

"""逆序取值"""
# 取值索引从 -1 倒着取值
print(name_list[-4])
print(name_list[-6])
