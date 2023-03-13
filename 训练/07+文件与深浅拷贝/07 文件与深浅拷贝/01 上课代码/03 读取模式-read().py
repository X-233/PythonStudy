f = open('my.txt', mode='r', encoding='utf-8')

# read() 一次性读取文件中所有数据
# 如果传参数, 那就是指定字符数量读取数据
txt = f.read(3)
print(txt)
f.close()