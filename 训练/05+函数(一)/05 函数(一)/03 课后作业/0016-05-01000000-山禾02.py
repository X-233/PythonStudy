"""
定义一个函数, 实现登录的功能

    要求: 现在有用户名(user_name)  密码(password)  两个变量
        如果用户输入正确的用户名和密码, 提示 "登录成功"
        如果用户输入错误的用户名和密码, 提示 "用户名或密码输入错误"
        如果用户输入三次错误, 提示 "您输入错误的次数过多,登录异常", 退出函数运行
        
    提示: 循环  +   逻辑判断
"""
def fun1():
    sum1 = 3
    while sum1:
        sum1 -= 1
        user_name = input('用户名:\n')
        password = input('密码:\n')
        if user_name == 'shanhe' and password == '123456':
            return print('登录成功')
        else:
            print('用户名或密码输入错误')
    return print('您输入错误的次数过多,登录异常')

user_name = 'shanhe'
password = '123456'

"""请在下方实现代码"""

if __name__ == '__main__':
    fun1()

