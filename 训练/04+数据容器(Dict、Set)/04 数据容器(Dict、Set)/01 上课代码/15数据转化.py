"""
数据类型转化
    int, float, str     bool 类型转化比较特殊
    list, tuple, set,   str, dict 转化的时候比较特殊
"""

print(int(5.0), int('5'), int(True))
print(float(5), float('5.0'))
print(str(5), str('5.5'), str(True), str(False))  # str <-> bool 转化时不可逆的

print(list('hello world !'), list((1, 2, 3, 4)), list({1, 2, 3, 4}))
print(tuple('hello world !'), tuple([1, 2, 3, 4]), tuple({1, 2, 3, 4}))
print(set('hello world !'), set([1, 2, 3, 4]), set((1, 2, 3, 4)))

# str <--> list

char1 = 'hello world !'
arr = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', '!']
print(arr)
print(str(arr))
print(''.join(arr))

person = {
    'name': '正心',
    'gender': '男',
    'age': 18,
}

keys = list(person.keys())
values = list(person.values())
print(keys, values)
rets = []
rets2 = {}
for index in range(len(values)):
    rets.append([keys[index], values[index]])
    rets2[keys[index]] = values[index]
print(rets)
print(rets2)
print(dict(rets))
