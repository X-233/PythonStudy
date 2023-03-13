"""
编写一个函数，判断一个数是否为素数，然后调用该函数输出100以内的素数

素数的定义: 在大于1的自然数（到无穷大的整数）中，除了1和它本身以外不再有其他因数。
"""

def func(num):
    """
    判断传入的数字是不是素数
    :param num: 传进来的数字
    :return: None
    """

    if num > 1:
        for j in range(2, num):  # j 取值范围是 2-8
            if num % j == 0:  # 如果满足这个条件, 代表当前这个数字除了1和本身之外有其他的因数, 那这个数字就不是素数
                print(f'该数字{num}不是素数')
                break  # 一旦满足if, 就结束循环

        else:  # 当一个循环是正常结束的, 那么就会执行else语句, 筛选范围中所有的素数
            print(f'{num} 是素数')

    else:
        print(f'该数字{num}不是素数')

func(56)
func(57)
func(91)
func(61)
func(13)
func(49)

# Shift + Tab  反缩进