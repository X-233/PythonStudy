"""

假设有以下地址:

    https://www.bbsmax.com/A/?user=7001&id=1305
    https://www.bbsmax.com/A/?user=7002&id=1306
    https://www.bbsmax.com/A/?user=7003&id=1307
    https://www.bbsmax.com/A/?user=7004&id=1308
    https://www.bbsmax.com/A/?user=7005&id=1309
    https://www.bbsmax.com/A/?user=7006&id=1310
    https://www.bbsmax.com/A/?user=7007&id=1311
    https://www.bbsmax.com/A/?user=7008&id=1312
    https://www.bbsmax.com/A/?user=7009&id=1313
    https://www.bbsmax.com/A/?user=7010&id=1314

观察以上地址规律, 将以上规律用循环构建出来
"""
user_count = range(7001, 7011)
id_count = range(1305, 1315)

print(list(user_count))
print(list(id_count))

print(list(zip(user_count, id_count)))
for user, id in zip(user_count, id_count):
    print(f'https://www.bbsmax.com/A/?user={user}&id={id}')


string = 'https://www.bbsmax.com/A/?user=70{0}&id=13{1}'
html_list = [string.format(array if array > 9 else '0' + str(array), array + 4 if array + 4 > 9 else '0' + str(array + 4)) for array in range(1, 11)]