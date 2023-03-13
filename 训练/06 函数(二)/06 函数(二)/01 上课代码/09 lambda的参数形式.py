# 无参数
fn1 = lambda: 100
print(fn1())

# 一个参数
fn2 = lambda a: a
print(fn2('你好'))

# 默认参数
fn3 = lambda a, b, c=100: a + b + c
print(fn3(10, 20))

"""不定长参数"""
fn4 = lambda *args: args
print(fn4(10, 20, 30))

fn5 = lambda **kwargs: kwargs
print(fn5(a=10, b=20, c=30))

fn6 = lambda *args, **kwargs: (args, kwargs)
print(fn6(1, 2, 3, a=10, b=20, c=30))
