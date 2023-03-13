import copy  # 深浅拷贝模块, 内置

array = [1, 2, 3, 4, 5]

# 浅拷贝会新建一个对象, 区分原对象的
arr1 = copy.copy(array)  # 将 array 这个对象完全浅拷贝一份出来


"""这两个变量任然是同一对象"""
print(id(array))
print(id(arr1))


# 修改一个对象值, 也导致另一个变量的结果也会改变
array[0] = 'a'

print(array)
print(arr1)

print('-------------浅拷贝的作用域------------')
array2 = [1,
          ['a', 'b', 'c'],
          3]

arr2 = copy.copy(array2)

array2[1][0] = 100

print(array2)
print(arr2)

# 浅拷贝仅作用域一维数据, 就是没有嵌套
# 如果浅拷贝数据中有嵌套数据, 那么拷贝出来的内容中嵌套的数据部分任然指得是统一对象

# [ 一维
#     [  # 二维
#         [1,2,3] # 三维
#      ]
# ]
