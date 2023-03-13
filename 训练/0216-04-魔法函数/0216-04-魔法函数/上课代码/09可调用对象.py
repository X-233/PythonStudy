class Example:
    def __call__(self, *args, **kwargs):
        return 'hello world !'


e = Example()
# 默认情况下 对象不能直接调用
print(e())  # __call__ 可以把对象当做方法进行调用

"""
    整个 python 的逻辑都是建立在魔法函数之上的
    理解魔法函数之后, 可以优化代码, 可以看懂更多的代码
    相当于 python 语言的核心语法
"""
