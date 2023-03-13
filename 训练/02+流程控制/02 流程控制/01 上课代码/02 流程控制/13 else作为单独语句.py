
for i in range(5):

    if i == 3:
        continue  # 循环一旦break了, 就不属于正常结束
                  # continue 属于正常结束的循环

    print(i)

else:
    print('我是else, 当循环正常结束我就会被执行')