def gen(ret=0):
    while True:
        agr = yield ret
        ret += 1
        print('接受的外部参数', agr)


g = gen()
print(next(g))

print(next(g))  # send 发送数据
print(g.send('World'))
print(g.send('!'))
