"""in 成员运算符"""

print('h' in 'hello world !')
print('h' not in 'hello world !')

print('hello' in ['hello', 'world !'])
print('hello' not in ['hello', 'world !'])

# 字典默认判断的是键
print('name' in {'name': '正心'})
print('正心' in {'name': '正心'})

"""is 身份运算符"""

number1 = 1
number2 = True
print('------------')
print(number1 == number2)  # number1 与 number2 的值是相等的
print(number1 is number2)  # number1 与 number2 并不是同一个东西
print(id(number1))  # id 是查看变量在内存当中的地址
print(id(number2))
# == 符号只是判断名字是否一样, is 是检查身份证号码是不是一样
