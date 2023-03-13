class Women:
    def __init__(self, name, high, age):
        self.name = name
        self.high = high
        # 双下划线代表私有属性 类的外部无法调用, 类的内部可以用引用
        self.__age = age

    # 双下划线代表私有方法 类的外部无法调用, 类的内部可以用引用
    def __return_info(self):
        print(self.__age)
        return self.__age

    def info(self):
        self.__return_info()  # 类的内部可以用引用私有方法


muzi = Women('木子', 165, 18)
# print(muzi.age)
# muzi.return_info()

# 私有属性和私有方法的作用是为了数据安全去考虑的, 避免数据泄露
