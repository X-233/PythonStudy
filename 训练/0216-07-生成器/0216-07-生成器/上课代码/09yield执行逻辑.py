def gen(n):
    print('3. 第一次会从最上面开始运行')
    index = 0
    while index < n:
        print(f'4.8 yield 返回内容 index={index}')
        yield index * index  # 返回内容之后会挂起
        print('7. 再次迭代的时候唤醒挂起的程序,继续进行迭代')
        index += 1


print('1. 创建一个生成器对象')
g = gen(4)
print(g)
print('2. 进行第一次迭代')
r = next(g)
print('5. 拿到回调的内容 r', r)  # 迭代第一个元素
print('6. 进行第二次迭代')
r = next(g)
print('5.9. 拿到回调的内容 r', r)
print(next(g))
print(next(g))
print(next(g))


"""
    激活阶段
    执行阶段
"""