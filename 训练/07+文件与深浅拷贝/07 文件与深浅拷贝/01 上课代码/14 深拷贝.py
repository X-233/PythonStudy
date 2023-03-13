import copy

array2 = [1,
          ['a', 'b', 'c'],
          3]

# copy.deepcopy 深拷贝, 把对象里面各个维度的数据全部拷贝一份, 区分原对象
arr2 = copy.deepcopy(array2)

array2[1][0] = 100

print(array2)
print(arr2)
