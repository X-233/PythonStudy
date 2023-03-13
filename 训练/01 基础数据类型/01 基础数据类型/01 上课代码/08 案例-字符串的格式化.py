"""
    猫眼top100的网址
    第一页：https://maoyan.com/board/4?offset=0
    第二页：https://maoyan.com/board/4?offset=10
    第三页：https://maoyan.com/board/4?offset=20
    ....
    第十页：https://maoyan.com/board/4?offset=90

    请分别使用三种字符串构建的方法创建所有的请求地址
"""

# """f"""
# for page in range(0, 91, 10):
#     base_url = f'https://maoyan.com/board/4?offset={page}'
#     print(base_url)

# """format"""
# for page in range(0, 91, 10):
#     base_url = 'https://maoyan.com/board/4?offset={}'.format(page)
#     print(base_url)

"""%s"""
for page in range(0, 91, 10):
    base_url = 'https://maoyan.com/board/4?offset=%s' % page
    print(base_url)