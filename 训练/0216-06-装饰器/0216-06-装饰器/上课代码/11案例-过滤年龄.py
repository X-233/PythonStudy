"""
定义一个用户模型（User）
    属性：姓名，年龄

定义一个方法：watch_movie。方法接收一个用户，
调用方法后打印 用户姓名、年龄、正在看电影
"""


class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def decorator(func):
    def wrapper(*args, **kwargs):
        # print(args, kwargs)
        user = kwargs.get('user')
        if user.age < 18:
            raise Exception(f'{user.name} 未满18不能看电影')
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator
def watch_movie(user):
    print(f'{user.name} 正在看电影')


user1 = User('张三', 17)
user2 = User('李四', 18)

try:
    watch_movie(user=user1)
except Exception as e:
    print(e)
watch_movie(user=user2)
