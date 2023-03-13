import requests

response = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
data = response.content
print(data)

# wb  write binary
# 二进制数据没有编码
with open('C:\\老师文件夹\\山禾\\baidu.png', mode='wb') as f:
    f.write(data)
