def get_weight_3(*args, **kwargs):
    print(args)
    print(type(args))

    print(kwargs)
    print(type(kwargs))



print(get_weight_3(80, 90, 120, a=100, b=200, c=300))
# 不定长参数常见于Python源码
