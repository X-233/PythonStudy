from collections.abc import Iterable

file = open('01基本概念.py', mode='r', encoding='utf-8')
print(isinstance(file, Iterable))
for line in file:
    print([line])
