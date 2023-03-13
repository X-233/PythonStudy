# 需求1：把code文件夹所有文件重命名 Python_xxxx
# 需求2： 删除Python_ 重命名：1， 构造条件的数据 2. 书写if
import os

os.chdir('code')  #  修改操作路径

# flage 控制需求实现
flag = 2

file_list = os.listdir()
print(file_list)

for i in file_list:
    if flag == 1:
        new_name = 'Python_' + i

    elif flag == 2:
        num = len('Python_')
        new_name = i[num:]

    # 重命名
    os.rename(i, new_name)
