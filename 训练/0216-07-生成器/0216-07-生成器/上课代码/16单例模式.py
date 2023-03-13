class MusicPlayer:  # 类对象只能创建一个实例对象
    _instance = None  # 类属性用于记录实例对象

    def __new__(cls):
        if cls._instance is None:  # 如果还没有创建过程序的实例对象
            cls._instance = object.__new__(cls)  # 就创建一个新的实例对象
        return cls._instance  # 返回程序的实例对象

    def __init__(self):
        pass


# 单例模式
play1 = MusicPlayer()
play2 = MusicPlayer()
play3 = MusicPlayer()

print(id(play1), id(play2))
print(play1 is play2)
