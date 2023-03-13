
# with 会有自己的代码块
# 当文件对象引用完毕以后会自动帮助我们关闭文件
# 用来偷懒用的

# as 将打开的文件对象取一个别名
with open('text.txt', mode='a', encoding='utf-8') as f:
    f.write('你好\n')