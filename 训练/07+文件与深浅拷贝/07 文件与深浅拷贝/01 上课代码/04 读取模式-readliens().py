f = open('my.txt', mode='r', encoding='utf-8')

"""
    readlines 可以按照行的方式把整个文件中所有的内容一次性读取
    返回一个列表, 期中每一行的数据数据为一个列表元素
"""
txt = f.readlines()
print(txt)
f.close()