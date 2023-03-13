array = [1, 2, 3, 4, 5]

arr1 = array  # 通过赋值的方式把对象进行了引用

"""这两个变量任然是同一对象"""
print(id(array))
print(id(arr1))


# 修改一个对象值, 也导致另一个变量的结果也会改变
array[0] = 'a'

print(array)
print(arr1)