
# 在定义函数的时候, 针对参数用等于号赋值, 那么就是设置这个参数的默认值
def f(k, x=5, b=6):  # 定义的时候位置参数放最前, 默认参数放最后 <约定俗成>
    y = k * x + b
    return y

# 针对位置参数传参, 默认参数没有传参, 那么在实际调用的时候, 函数会使用默认参数的值
print(f(9))
# 如果用未知参数把所有的参数都传递了, 那么会修改默认参数的值
print(f(5, 6, 7))
# 用关键字参数, 指定参数的名字, 可以修改默认参数的值
print(f(5, x=6, b=7))

# 如果在修改的时候, 有的参数制定了参数名, 有的参数没有, 那么需要把没有名字的位置参数放最前面
# print(f(5,b=7, 6))
