
num = 10  # 定义的一个全局变量


def foo():
    # 函数内部使用的变量是属于局部变量
    # 函数内部的变量作用域函数内部
    # 整个函数的作用域仅作用域函数内部
    # global num  # 代表申明操作全局变量, global 尽量不要用
    num = 20
    print('函数里面输出的num:', num)
    return num

foo()

print(num)