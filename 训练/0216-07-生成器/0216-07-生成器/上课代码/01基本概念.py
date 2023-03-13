arr = ['a', 'b', 'c', 'd']

"""while 循环"""
index = 0
while index < len(arr):
    print(arr[index])
    index += 1
"""for 循环"""
print('----for 循环----')
for index in range(len(arr)):
    print(arr[index])  # for 循环是通过索引取值

"""for 遍历"""
print('----for 遍历----')
for item in arr:
    print(item)

"""递归"""

print('---函数递归---')


def func(arr, index):
    if index == len(arr):
        return
    print(arr[index])
    func(arr, index + 1)


func(arr, 0)
