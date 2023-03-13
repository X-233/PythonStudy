class Son(object):
    def __new__(cls, *args, **kwargs):
        """"""
        """
            在__init__方法调用之前, 会调用__new__方法创建一个实例对象
        """
        # object 原始基类
        # object.__new__ 创建一个实例对象
        # cls 当前的类对象
        instance = object.__new__(cls)  # 以当前的类对象(cls)为模板创建一个实例对象
        # cls 类对象自己本身
        print('__new__ 方法被调用了', instance)  # 能不能在这里调用实例属性
        return instance

    def __init__(self, name):
        """初始化方法 我是谁"""
        """
            初始化方法 --> 魔法函数, 都是在背后自动调用
            创建实例对象的时候,会自动调用
            可以给实例对象初始化一些属性
        """
        self.name = name
        print('__init__ 方法被调用了', self)

    def __del__(self):  # 相当于死亡宣告
        print('__del__ 被调用了')


son = Son('大头儿子')  # 实例化一个对象的时候, 会自动调用 __init__ 方法

print(son.name)

"""
1. __new__     用于创建实例对象
2. __init__    用于初始化实例对象
3. __del__     用于释放实例对象

魔法方法大多数时候都是自动调用的
"""
