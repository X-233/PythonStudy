# lambda 两个数字比大小，谁大返回谁

func1 = lambda a, b: a if a > b else b
print(func1(1000, 500))
print(func1(10000, 9999))
