# file = open('01基本概念.py', mode='r', encoding='utf-8')
# lines = file.readlines()
# file.close()

# with open('01基本概念.py', mode='r', encoding='utf-8') as file:
#     lines = file.readlines()
#     # file.close()
# print('结束 with 之后会自动调用 file.close()')

class File:
    def __init__(self, filename, mode='r', encoding='utf'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        print('进入上下文管理器')
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print('退出上下文管理器')


input('输入任意内容进入上下文管理器')
with File('01基本概念.py', mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    input('输入任意内容结束上下文管理器')
input('输入任意内容结束程序')
