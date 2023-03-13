# 之前学习到的知识 函数是不可以在继续分
import asyncio

import requests


def get_html(html=None):
    while True:
        url = yield html
        print('请求地址', url)
        if url == 'exit':
            yield 'exit'
            raise StopIteration
        html = requests.get(url).text


def parse_html(data=None):
    while True:
        html = yield data
        print('解析数据', [html])
        if html == 'exit':
            yield 'exit'
            raise StopIteration
        data = html.split()


url = 'http://www.baidu.com/?page='


def mian():
    g_get_html = get_html()
    g_parse_html = parse_html()
    print(next(g_get_html))  # 第一次需要用next激活生成器对象
    print(next(g_parse_html))
    index = 1
    while True:
        # g_get_html 是什么 生成器对象 回调之后才能拿到生成器对象里面的结果
        html = g_get_html.send(url + str(index))  # send 需要传递参数 next等价于 .send(None)
        data = g_parse_html.send(html)
        # data 是最终处理的结果,应该保存到文件里面
        index += 1


async def get():
    await asyncio.sleep(1)


if __name__ == '__main__':
    mian()

"""
    通过 yield 实现在函数之间的切换, 是协程的原理
"""
