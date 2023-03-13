

""" +  增加文件的权限"""

f = open('my.txt', mode='r+', encoding='utf-8')

f.write('123')
print(f.read())

f.close()