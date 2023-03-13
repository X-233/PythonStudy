#  \n 换行符号
# 查看源码的快捷键  Ctrl + 鼠标左键点击进入
s = '\n # hello world ! # \n'
print(s)

"""strip 去除字符串两端的空白字符"""  # 仅作用于字符串前后两端
print('-------------strip 去除字符串两端的空白字符-------------')
print(s.strip())
print(type(s.strip()))  # 对象就有对象的方法和属性
print(s.strip().strip('#'))
# strip 返回的类型也是字符串


""" replace 替换"""
print('-------------replace 替换-------------')
# print(s.replace('#', '?'))
# replace 返回的类型也是字符串
print(s.replace('#', '?').replace('\n', '$').replace('!', '+'))


"""split 分割"""
print('-------------split 分割-------------')
# spilit 默认以空白字符进行分割, 返回一个列表
print(s.split())
print(type(s.split()))
# 可以指定字符进行分割
# print(s.split('#').replace('!', '+'))

# Python要根据类型执行相关的操作


"""join 合并字符串"""
print('-------------join 合并字符串-------------')
# python区分大小写, 以及中英文符号
s = '张三，李四，王五'
print(s.split('，'))

# 用 ? 号作为分割符把列表列表里面的元素合并成一个新的字符串
print('?'.join(s.split('，')))