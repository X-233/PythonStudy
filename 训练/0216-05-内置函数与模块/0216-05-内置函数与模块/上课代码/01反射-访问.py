print(id(id))
one = 1
two = 1
print(id(one))
print(id(two))
print(one is two)
# python 内存驻留机制

arr1 = [1]
arr2 = [1]
print(id(arr1))
print(id(arr2))

# 获取对象的长度
print(len([1, 2, 3]))
print(arr1[0])
print(id(arr1[0]))

# 获取对象的拥有的方法
print(dir(list))
import pygame

print(dir(pygame))

# type 查看对象的类型
print(type(1))
print(type('1'))
