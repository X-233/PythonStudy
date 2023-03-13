# """ r 只读模式"""
# f = open('my.txt', mode='r')
# f.write('你好')
# txt = f.read()  # read() 一次性读取文件中所有数据
# print(txt)
# f.close()


# """ w 只写模式"""
# # w  只写, 如果文件不存在, 新建文件; 如果文件存在就会直接在文件中写入数据
# # w 模式在写数据之前会把文件中所有数据清空后再写入
# f = open('my.txt', mode='w', encoding='utf-8')
# f.write('你好\n')
# f.write('我好\n')
# f.write('大家好\n')
# # txt = f.read()  # read() 一次性读取文件中所有数据
# f.close()

""" a 追加模式"""
# a  追加模式, 如果文件不存在, 新建文件; 如果文件存在就会直接在文件末尾写入数据
f = open('my.txt', mode='a', encoding='utf-8')
f.write('你好\n')
f.write('我好\n')
f.write('大家好\n')
txt = f.read()
f.close()

"""
    w : 只写, 如果文件不存在, 新建文件; 如果文件存在就会直接在文件中写入数据. 将旧数据覆盖
    a : 追加, 如果文件不存在, 新建文件; 如果文件存在就会直接在文件末尾写入数据, 旧数据会保留
"""