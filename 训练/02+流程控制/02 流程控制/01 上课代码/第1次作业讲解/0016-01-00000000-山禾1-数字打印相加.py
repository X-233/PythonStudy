"""
输入两个数字（input）,相加之后打印输出
"""

# input --> 输入函数  print --> 输出结果函数

num1 = int(input('请输入第一个数字'))  # input函数返回的数据类型都是 字符串类型
num2 = float(input('请输入第二个数字'))

print(type(num1))

# 注意Python中数据类型  # 字符串与字符串相加是拼接字符串
result = num1 + num2
print(result)

# Python中的类型转化, 用类型的关键字转化 str()  int()  float()
