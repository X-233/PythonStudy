# 内置作用域 内置函数 内置模块
# int


# 全局作用域 自己定义的变量 函数
pi = 3.14


def foo():
    # pi 是函数里面的局部作用域
    pi = 3.15

    def printer():
        # printer 是嵌套函数
        print('printer pi', pi)
        # 可以继续嵌套函数吗?

    print('foo pi', pi)
    printer()


print('global pi', pi)
foo()
# 可以在全局变量调用、修改函数内部的变量与函数吗？ 不可以
# 默认的情况下，函数运行完之后里面的内容会被全部回收
