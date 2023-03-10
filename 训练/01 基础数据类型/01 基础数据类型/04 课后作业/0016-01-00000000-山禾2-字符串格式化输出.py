"""
请用一个字符串模板（三种格式化），输出以下结果
（只要能实现效果就行，不限制实现方式）

python 是一门动态解释型语言，起源于1989年圣诞节期间
Java 是一门静态编译型语言，起源于1991年
C 是一门静态编译型语言，起源于1969年到1973年期间
"""
s1 = "{} 是一门{}语言，起源于{}年{}"

args1 = ("Python", "动态解释型", 1989, '圣诞节期间')
args2 = ("Java", "静态编译型", 1991, '')
args3 = ("C", "静态编译型", '1969年到1973', '期间')

"""自己在下方编写代码实现功能"""
# str_1 = s1.format(args1[0], args1[1], args1[2], args1[3])
str_1 = s1.format(*args1)

# str_2 = s1.replace('{}', '%s') % (args2[0], args2[1], args2[2], args2[3])
str_2 = s1.replace('{}', '%s') % args2

str_3 = f'{args3[0]} 是一门{args3[1]}语言，起源于{args3[2]}年{args3[3]}'

print(str_1)
print(str_2)
print(str_3)
