# -*- coding: utf-8 -*-
"""
作业4：
统计Python之禅中所有**单词**(注意是单词)出现的次数
"""
# python 之禅
s = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Flat is better than nested
Sparse is better than dense
Readability counts
Special cases aren't special enough to break the rules
Although practicality beats purity
Errors should never pass silently
Unless explicitly silenced
In the face of ambiguity, refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it
Although that way may not be obvious at first unless you're Dutch
Now is better than never
Although never is often better than *right* now
If the implementation is hard to explain, it's a bad idea
If the implementation is easy to explain, it may be a good idea
Namespaces are one honking great idea -- let's do more of those
"""


"""自己在下方编写代码实现功能"""

result = s.replace('-', '').replace('*', '').replace(',', '')
print(result)
print(result.split())


d = {}
for char in result.split():
    if char not in d.keys():
        d[char] = 1

    else:
        d[char] += 1

    print(d)
