import requests
import threading

lock = threading.Lock()
# response = requests.get('http://www.baidu.com/')
# print(response.status_code)


with requests.get('http://www.baidu.com/') as response:
    print(response.status_code)
