name_list = ['正心', '丸子', '自游', '巳月']

# 列表.append(需要添加的数据)   --> 通过append方法值将数据添加到列表的尾部
name_list.append('清风')

print(name_list)


"""
列表是一种可变的数据类型, 操作过程都是基于列表本身
"""

# 如果追加是一个列表, 那么会把整个列表作为一个数据, 追加到列表尾部
name_list.append(['清风', '木子'])
print(name_list)


"""如果不想要把整个列表作为一个元素追加, 那么需要用 extend() 列表的合并"""
name_list2 = ['正心', '丸子', '自游', '巳月']
name_list3 = ['清风', '木子', '丸子']
name_list2.extend(name_list3)  # 把 name_list3 列表数据合并到 name_list2 尾部
print(name_list2)



"""指定位置添加数据到列表"""
name_list4 = ['正心', '丸子', '自游', '巳月']
# 传递两个参数, 第一个参数是你要在列表的哪里插入数据(索引), 第二个参数你插入的数据是什么
name_list4.insert(2, '清风')
print(name_list4)
