
# 收集以下列表中所有不重复的数据

list1 = [4, 2, 1, 0, 6, 2, 1]


list2 = []  # 空列表收集的就是所有不重复的数据
# range(7)  0123456
for index in range(len(list1)):  # 遍历列表中数据索引
    if list1[index] not in list2:
        list2.append(list1[index])

    else:
        print('重复数据:', list1[index])
        print('    重复索引:', index)

print(list2)
