""""""
"""
    gbk 
        一个中文占三个字节 byte
    utf-8 编码
        一个中文占四个字节 byte
    
    0000        0
    0001        1
    0010        2
    ...         ..
    1110        e
    1111        f
"""

message = '晚'

print(message.encode('gbk'))
print(message.encode('utf-8'))

"""
    一本小说是 10mb , 大概会有多少个汉字 (utf-8编码, 一个汉字是四个byte计算)
"""
