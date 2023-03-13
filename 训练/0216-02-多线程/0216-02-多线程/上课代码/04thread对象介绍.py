import threading


def function(*args, **kwargs):
    print(args)
    print(kwargs)


# 多线程的作用是将 普通对象 变成 多线程对象

# function(1, 2, 3, 4, a=6, b=7)
"""
    target: 目标函数, 需要将那个普通对象变成多线程对象
    args:   位置参数, 用元祖进行传递
    kwargs: 关键字参数
"""
# 必须以关键字的形式进行传参
thread_function_obj = threading.Thread(target=function, args=(1, 2, 3, 4), kwargs={'a': 6, 'b': 7})
thread_function_obj.start()
