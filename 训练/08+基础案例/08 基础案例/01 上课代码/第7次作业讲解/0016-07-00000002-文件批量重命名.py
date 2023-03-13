"""
请在当前py文件中编辑代码
将code文件夹中为文件名字后面添加 "-python", 文件尾缀不变
"""

import os

# change
os.chdir('code')  # 改变文件操作路径

print(os.listdir())

for i in os.listdir():
    # print(i)
    # 构造一个新的文件名字
    name_index = i.index('.')
    new_name = i[:name_index] + '-python' + i[name_index:]
    print(new_name)

    os.rename(i, new_name)





