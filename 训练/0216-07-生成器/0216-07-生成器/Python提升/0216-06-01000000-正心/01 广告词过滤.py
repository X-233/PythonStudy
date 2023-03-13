"""
参考备课代码，写出一个用户名敏感词过滤装饰器，需要过滤敏感词见 `敏感词表(广告).txt`

要求使用函数装饰器实现，在实例化对象时，一旦名字中出现在敏感词表中的内容，提示不能创建对象（或抛出异常）。
"""


class User:
    """用户模型"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


def watch_movie(user=None):
    """观看电影的方法"""
    print("%s 名字正常" % user)


# 想看的一个陌生的代码
# 1. 实例化对象
user1 = User('张三', 17)
user2 = User('李四', 18)
user3 = User('兼职', 18)

# 2. 传入用户对象 调用方法
watch_movie(user=user1)
watch_movie(user=user2)
watch_movie(user=user3)
