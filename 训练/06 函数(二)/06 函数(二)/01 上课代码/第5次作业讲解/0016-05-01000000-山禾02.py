"""
定义一个函数, 实现登录的功能

    要求: 现在有用户名(user_name)  密码(password)  两个变量
        如果用户输入正确的用户名和密码, 提示 "登录成功"
        如果用户输入错误的用户名和密码, 提示 "用户名或密码输入错误"
        如果用户输入三次错误, 提示 "您输入错误的次数过多,登录异常", 退出函数运行
        
    提示: 循环  +   逻辑判断
"""


user_name = 'shanhe'
password = '123456'

"""请在下方实现代码"""

def login():

    count = 0  # 记录输入错误信息的次数
    while True:
        user = input('请输入用户名:')
        pwd = input('请输入密码:')

        if user == user_name and pwd == password:
            print('登陆成功')
            break
            # return None

        if user != user_name or pwd != password:
            print('用户名或密码输入错误')
            count += 1

        if count >= 3:
            print('您输入错误的次数过多,登录异常')
            return None

login()