# 文件名备份规则   旧的文件名 + [备份] + '尾缀'

old_name = input('请输入您需要备份的文件名:')


# 2. 规划备份文件的名字
index = old_name.index('.')
print('点在文件名中的索引位置', index)

new_name = old_name[:index] + '[备份]' + old_name[index:]
print(new_name)

"""读取旧文件数据"""
with open(old_name, mode='rb') as file:
    data = file.read()


"""写入到备份文件"""
with open(new_name, mode='wb') as f:
    f.write(data)
