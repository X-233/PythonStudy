# arr = []
#
# # [1, 4, 9, .... , 81]
# for index in range(1, 10):
#     # 1 2 3 ... 9
#     if index % 2 == 0:
#         arr.append(index * index)
#
# print(arr)
# 列表推导式  -- 推导式生成的元素本身就在列表里面
arr2 = [index * index for index in range(1, 10)]
print(arr2)
arr3 = [index * index for index in range(1, 10) if index % 2 == 0]
print(arr3)

# 列表推导式只能实现简单的推导功能

# 10 / 3 = 3 ... 1
# 10 % 3 == 1   # 取余
# 10 // 3 == 3  # 取整
