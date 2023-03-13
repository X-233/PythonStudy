"""
定义一个用户模型（User）
    属性：姓名，年龄

定义一个方法：watch_movie。方法接收一个用户，
调用方法后打印 用户姓名、年龄、正在看电影
"""
import time


class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def filter_age(func):
    def wrapper(*args, **kwargs):
        print('filter_age start')
        user = kwargs.get('user')
        if user.age < 18:
            raise Exception(f'{user.name} 未满18不能看电影')
        result = func(*args, **kwargs)
        print('filter_age end')
        return result

    return wrapper


def timer(func):
    def wrap(*args, **kwargs):
        print('timer start')
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        print('timer end')
        return result

    return wrap


# @filter_age
# @timer
def watch_movie(user):
    print(f'{user.name} 正在看电影')


# watch_movie = timer(watch_movie)
# watch_movie = filter_age(watch_movie)
watch_movie = filter_age(timer(watch_movie))

user1 = User('张三', 17)
user2 = User('李四', 18)

# try:
#     watch_movie(user=user1)
# except Exception as e:
#     print(e)
watch_movie(user=user2)
