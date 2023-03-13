"""
定义一个用户模型（User）
    属性：姓名，年龄

定义一个方法：watch_movie。方法接收一个用户，
调用方法后打印 用户姓名、年龄、正在看电影
"""


class User(object):
    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level


def filter_level_3(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if user.level < 3:
            raise Exception(f'{user.name} 的会员等级为 {user.level} 没有权限,请充值')
        result = func(*args, **kwargs)
        return result

    return wrapper


def filter_level_4(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if user.level < 4:
            raise Exception(f'{user.name} 的会员等级为 {user.level} 没有权限,请充值')
        result = func(*args, **kwargs)
        return result

    return wrapper


def filter_level(level):  # 缓存过滤等级
    def decorator(func):  # 缓存装饰函数
        def wrap(*args, **kwargs):  # 装饰函数
            user = kwargs.get('user')
            if user.level < level:
                raise Exception(f'{user.name} 的会员等级为 {user.level} 没有权限,请充值')
            ret = func(*args, **kwargs)
            return ret

        return wrap

    return decorator


def filter_level_5():
    return filter_level(5)  # filter_level(5) 才是实际的装饰器


# @filter_level_3
# @filter_level(3)
@filter_level_4
def watch_movie2(user):
    print(f'{user.name} 正在看电影')


user1 = User('张三', 17, 3)
user2 = User('李四', 18, 4)

try:
    watch_movie2(user=user1)
except Exception as e:
    print(e)
watch_movie2(user=user2)
