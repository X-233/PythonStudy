info_str = """龙猫

主演：秦岚,糸井重里,岛本须美

上映时间：2018-12-14"""
"""
需求：
    1. 拿到主演的姓名（列表）
    2. 将主演名字合并为字符串，中间用中文的逗号隔开
"""

result1 = info_str.split()
# print(result1[1])

name_str = result1[1]
result2 = name_str.strip('主演：')
# print(result2)
result3 = result2.split(',')
print(result3)

print('，'.join(result3))

