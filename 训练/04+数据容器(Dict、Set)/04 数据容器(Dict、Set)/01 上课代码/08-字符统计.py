import this

this_str = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 同统计 python 之禅里面每一个字符串出现的次数
d = {}
# 1. 统计所有出现过得字符串
for char in this_str:
    # print(char)
    # d[char] = 1
    # 2. 统计出现过的字符串出现的次数
    # 每次字符出现的次数分别为第 1 次 与第 N 次
    # 如果是第一次出现
    if char not in d.keys():
        d[char] = 1
    else:
        d[char] = d[char] + 1

print(d)
print(d.keys())

# 趣味性作业: 统计过去十年英语四级的高频词汇, 然后按照顺序排列下来
