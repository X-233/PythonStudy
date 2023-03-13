"""
请在当前py文件中编辑代码
将code文件夹中为文件名字后面添加 "-python", 文件尾缀不变
"""
import os

dir_1 = os.listdir('code')
dir_1.sort(key=lambda x: x.rsplit('.')[0])
os.chdir('code')
for i in dir_1:
    if '-python' not in i:
        os.rename(i, i.rsplit('.')[0] + '-python.' + i.rsplit('.')[-1])
    else:
        os.rename(i, i.split('-')[0] + '.' + i.rsplit('.')[-1])