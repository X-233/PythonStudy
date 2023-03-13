"""
*
**
***
****
*****

要打印的效果:正右三角形  5 - 行数
    *
   **
  ***
 ****
*****
"""
print('-------------正左三角形--------------')
for i in range(1, 6):  # 控制行数
    for j in range(i):  # 控制列数
        print('*', end='')
    print()

print('-------------正右三角形--------------')
for i in range(1, 6):  # 控制行数
    # 先打印空格
    space_num = 5 - i  # 每一行空格的数量
    for k in range(space_num):
        print(' ', end='')

    # 在打印小星星
    for l in range(i):
        print('*', end='')

    print()