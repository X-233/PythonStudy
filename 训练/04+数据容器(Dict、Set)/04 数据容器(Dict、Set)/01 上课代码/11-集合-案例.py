# 集合: 可变的 不可重复的(去重) 无序的 数据类型

char1 = 'hello world !'
char2 = 'hello python !'

set1 = set(char1)
set2 = set(char2)
# 两个字符串重复的部分
print(set1 & set2)
# 两个字符串不重复的部分
print(set1 ^ set2)
# 第一个字符串比第二个字符串多出来的部分
print(set1 - set2)
