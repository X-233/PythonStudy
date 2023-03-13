
i = 0

while i < 5:
    i += 1

    if i == 2:
        continue  # # 结束当前循环, 执行下一次循环
                  # 在嵌套循环中, 满足就近原则进行循环的中断
    print(i)
