arr = ['1', '2', 3, 4, 5, '6', '7']

"""
请将 arr 保存到本地文件

文件名为: hello.txt
文件内容: 1,2,3,4,5,6,7
"""

with open('hello.txt', 'w')as f:
    for i in arr:
        if isinstance(i, int):
            f.write(str(i))
        else:
            f.write(i)
        if arr.index(i) != len(arr) - 1:
            f.write(',')

