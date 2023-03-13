class Rect:  # 正方形
    def __init__(self, side):
        self.side = side

    @property  # 核心编程 面向对象 类与对象
    def area(self):
        return self.side * self.side

    # def __repr__(self):
    #     return f'<class Rect side: {self.side:.2f}>'

    def __del__(self):
        print(f'{id(self)} 对象被删除了')


rect = Rect(4)
rect2 = rect
print(rect)
input('输入任意内容删除rect对象')
del rect  # 在对象删除之前, 会通知一下 __del__ 方法
input('输入任意内容删除rect2对象')
del rect2  # 在对象删除之前, 会通知一下 __del__ 方法
input('输入任意内容结束程序')
# 当程序结束的时候会将内存全部释放, 在对象被删除之前会调用 __del__ 方法
