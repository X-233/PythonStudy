list1 = ['a', 'b', 'c', 'd', 'e']

index = 0
for item in list1:
    print(index, item)
    index += 1

print('----------')
for index, item in enumerate(list1):
    print(index, item)

# 0110 0001 --> 97  --> a
char = 'a'
print(char, ord(char), bin(ord(char)))
a = 0b1100001  # 0b 表示二进制
print(a, chr(a))
