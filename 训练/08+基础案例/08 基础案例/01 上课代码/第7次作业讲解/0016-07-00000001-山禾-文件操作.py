arr = ['1', '2', 3, 4, 5, '6', '7']

"""
请将 arr 保存到本地文件

文件名为: hello.txt
文件内容: 1,2,3,4,5,6,7
"""


# for i in range(len(arr)):
#     arr[i] = str(arr[i])
# print(arr)
#
# print(','.join(arr))
#
#
# [str(i) for i in arr]


for i in arr:
    with open('hello.txt', mode='a', encoding='utf-8') as f:
        # open 函数打开的文件对象只能操作字符串和二进制数据
        f.write(str(i))
        f.write(',')


