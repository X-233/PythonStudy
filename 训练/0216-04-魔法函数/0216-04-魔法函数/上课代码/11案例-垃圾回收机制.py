class Rect:  # 正方形
    def __init__(self, side):
        self.side = side

    @property  # 核心编程 面向对象 类与对象
    def area(self):
        return self.side * self.side

    def __del__(self):
        print(f'{id(self)} 对象被删除了')


def create_rect():
    # 局部作用域
    rect1 = Rect(5)  # 局部作用域一结束 就会被回收
    rect = Rect(4)  # 创建的时候 引用计数 +1
    input('输入任意内容结束函数')
    return rect, [rect]


global_rect, arr = create_rect()
# 在全局作用域有引用局部作用域的 rect 吗 ?
input('输入任意内容删除 global_rect')
del global_rect

input('输入任意内容覆盖')
# arr = []
arr[0] = 0
input('输入任意内容结束程序')

"""
    作用域
    
    调用函数,得到函数的结果
    
    对象引用 不是函数引用
"""