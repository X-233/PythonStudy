import os  # 内置

# rename(): 重命名  文件不存在就报错
# os.rename('测试', '不测试')

# remove(): 删除文件, 文件不存在就报错
# os.remove('不测试')

# mkdir()：创建文件夹
# os.mkdir('aa')

# rmdir(): 删除文件夹
# os.rmdir('不测试')

# getcwd(): 返回当前文件所在目录路径
# print(os.getcwd())

# os.mkdir('aa\\bb')

# chdir():改变目录路径
# os.chdir('aa')
# os.mkdir('bb')

# listdir(): 获取某个文件夹下所有文件，返回一个列表
# print(os.listdir())

if not os.path.exists('查找'):  # 如果 查找 这个文件夹不存在
    os.mkdir('查找')
# print(os.path.exists('查找'))

os.mkdir('查找')