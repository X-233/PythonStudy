"""
判断平年闰年：

	闰年的条件是: 满足其中一个条件就行
		一:能被4整除，但不能被100整除的年份(例如2008是闰年，1900不是闰年) 
		二:能被400整除的年份(例如2000年)也是闰年。
	
	反之都是平年。
	
请设计一个函数
	用户输入年份，传入函数中的参数
	在函数中判断输入的年份是平年还是闰年
"""

# def get_year(year):
#     if year % 4 == 0 and year % 100 != 0:
#         print('闰年')
#
#     elif year % 400 == 0:
#         print('闰年')
#
#     else:
#         print('平年')
#
#
# get_year(2023)


def get_year():  # 变量注解, 表明这个变量的类型


    while True:
        year = int(input('请输入年份:'))

        if year == 0:
            break

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print('闰年')

        else:
            print('平年')


get_year()
