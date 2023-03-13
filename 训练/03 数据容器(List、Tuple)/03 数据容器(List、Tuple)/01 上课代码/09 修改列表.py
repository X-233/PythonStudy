"""赋值修改"""
name_list = ['正心', '丸子', '自游', '木子']

# 根据索引找到列表中的数据, 可以赋值修改值
name_list[2] = '清风'
print(name_list)

"""反转列表"""
name_list.reverse()
print(name_list)

"""列表排序"""
num_list = [2, 4, 5, 3, 7, 5, 8]
num_list.sort()  # 默认升序排列
num_list.sort(reverse=True)  # reverse=True 降序排列
print(num_list)