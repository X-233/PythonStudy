name_list = ['正心', '丸子', '自游', '巳月']

name = input('请输入一个名字:')

if name in name_list:
    print(f'年输入的名字是 {name}, 名字存在!')
else:
    print(f'年输入的名字是 {name}, 名字不存在!')