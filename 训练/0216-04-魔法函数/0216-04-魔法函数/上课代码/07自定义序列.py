class FunctionalList:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __repr__(self):
        return str(self.values)

    def append(self, value):
        self.values.append(value)


func_list = FunctionalList([1, 2, 3, 4, 5, 6, 7, 8])

print(func_list)
print(func_list[-1])  # 列表取值 --> __getitem__
print(func_list[0:-1])  # 列表切片 --> __getitem__

del func_list[-1]  # __delitem__

func_list.append('a')
print(func_list)