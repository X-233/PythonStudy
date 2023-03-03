# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
import requests
import redis
from time import sleep
from random import random
import os
import shutil

# source_path = os.path.abspath('/漫画')
# target_path = os.path.abspath('D:/漫画')
# if not os.path.exists(target_path):
#     os.mkdir(target_path)

res = requests.get('https://docker.ka2000.xyz/')
print(res.status_code)



# r4 = redis.StrictRedis(host="180.76.187.206",
#                            port=6379,
#                            password="zhanglin",
#                            db=4,
#                            username="default")
# while True:
#     try:
#         i = r4.spop('IP_Best')
#     except:
#         break
#     i = i.decode('utf-8')
#     proxies = {
#         'http': i,
#         'https': i,
#     }
#     sleep(random()*2)
#     try:
#         res = requests.get('http://httpbin.org/get', proxies=proxies, timeout=None)
#
#         r4.sadd('IP_3', i)
#         print('#'*20)
#         print(res.text)
#         print(i)
#         print('#'*20)
#         res.close()
#     except requests.exceptions.ConnectionError as e:
#         # print('Error', e.args)
#         print(i)
# r4.close()

# re1 = requests.get('https://s2.baozimh.com/scomic/jiuweihuxiaobachengshangwozhihou-zhenzhukouyuanzhuboyimanhua/0/29-rv85/1.jpg', timeout=20)
# print(re1.status_code)
# with open('1.jpg', 'wb')as f:
#     f.write(re1.content)