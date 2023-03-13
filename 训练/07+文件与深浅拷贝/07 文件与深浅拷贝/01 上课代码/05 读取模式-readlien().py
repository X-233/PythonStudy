f = open('my.txt', mode='r', encoding='utf-8')

"""
    readline 调用一次此方法一次只读取文件中一行数据
    适合大文件的读取, while True
"""
# txt = f.readline()
# print('第一行:', txt)
#
# txt = f.readline()
# print('第二行:', txt)
#
# txt = f.readline()
# print('第三行:', txt)
#
# txt = f.readline()
# print('第四行:', txt)

while True:
    txt = f.readline()

    if txt == '':
        break

    print(txt)


f.close()