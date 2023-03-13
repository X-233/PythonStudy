import threading

import requests


def get_html(url):
    response = requests.get(url)
    return response.text


def proxy_get_html(url):
    html = get_html(url)
    print(html)


def save_html(html):

    # 只有保存的时候需要上锁, 因为是保存到同一个文件
    # 保存在不同的文件中需要上锁吗 ?  敏感操作可以在做程序设计的时候尽量避免
    with open('baidu.txt', mode='w', encoding='utf-8') as file:
        file.write(html)


def main(url):
    html = get_html(url)
    save_html(html)


urls = ['https://www.baidu.com?page=1', 'https://www.baidu.com?page=2']
for url in urls:
    # html = get_html(url)
    # print(html)

    # get_html 任务有返回值
    """
        多线程对象将 普通对象 变成多线程对象, 没有返回值
        解决办法: 写一个代理函数处理返回值
    """
    # get_html_thread = threading.Thread(target=get_html, args=(url,))
    # get_html_thread = threading.Thread(target=proxy_get_html, args=(url,))
    # get_html_thread.start()

    # 需要将两个函数都变成多线程对象 ?
    # html = get_html(url)
    # save_html(html)  # 请求与保存是一个整体
    threading.Thread(target=main).start()

    # threading.Thread(target=get_html, args=(url,)).start()
    # threading.Thread(target=save_html, args=(html,)).start()
