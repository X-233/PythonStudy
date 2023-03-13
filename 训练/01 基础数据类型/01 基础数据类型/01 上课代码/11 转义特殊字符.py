"""特殊字符的转义"""

print('hello \n world')

# \  代表转义字符, 作用: 将具有特殊含义的字符串转义成普通字符串
print('hello \\n world')
print("hello \\n world")

# C:\\Env\\Anaconda3  # \ 也是属于特殊字符, 在文件路径显示会用

print("hello \t\t world")
print("hel \t\t world")  # \t 制表符号

# r 在字符串前面加上, 表示原生字符串, 原生字符串中所有字符都是普通字符串
print(r"hel \t\t world")