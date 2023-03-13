"""
复利公式：s = p(1 + i)^n

s 是本金 + 利息
p 本金
i 利率
n 投资年限

余额宝 兴全添利宝 年化 2.5610%
假设本金（principal）10000
1、请问分别存 5年 10年 15年 20年后 本金利息共多少
2、如果利率（interest）变成 6% 分别存 5年 10年 15年 20年后 本金利息共多少
3、如果本金变成 20000，利率不变 分别存 5年 10年 15年 20年后 本金利息共多少
"""


def func(p, i, n):
    s = p * (1 + i) ** n
    return s


principal = 10000
interest = 2.561 / 100

print(func(principal, interest, 5))
print(func(principal, interest, 10))
print(func(principal, interest, 15))
print(func(principal, interest, 20))
print('----------------------------------')

print(func(principal, 6 / 100, 5))
print(func(principal, 6 / 100, 10))
print(func(principal, 6 / 100, 15))
print(func(principal, 6 / 100, 20))
print('----------------------------------')

print(func(20000, 6 / 100, 5))
print(func(20000, 6 / 100, 10))
print(func(20000, 6 / 100, 15))
print(func(20000, 6 / 100, 20))
