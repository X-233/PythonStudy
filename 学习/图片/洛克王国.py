# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import os
from concurrent.futures import ThreadPoolExecutor
import requests
from tqdm import tqdm
from lxml import etree
import parsel


def header():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    if not os.path.exists('D:\\图片\\洛克王国'):
        os.mkdir('D:\\图片\\洛克王国')
    os.chdir('D:\\图片\\洛克王国')
    return headers


def analysis(url_1):
    html = requests.get(url=url_1, headers=header())
    html.encoding = html.apparent_encoding
    select = parsel.Selector(html.text)
    list_1 = select.xpath('//*[@class="wall_box"]')
    img_url = {}
    for i_1 in list_1:
        list_img = []
        list_2 = i_1.xpath('./ul/li')
        img_path = i_1.xpath('.//*[@class="wall_top_title"]/text()').get()
        # print(img_path)
        for j in list_2:
            x = j.xpath('./p/a[2]/@href').get()
            y = j.xpath('./p/a[1]/@href').get()
            if x is not None:
                list_img.append(x)
                # print(x)
            if y is not None:
                list_img.append(y)
                # print(y)
        img_url[img_path] = list_img
    return img_url


def down_img(path, url_2):
    if not os.path.exists(path):
        os.mkdir(path)
    img = requests.get(url=url_2, headers=header(), timeout=7)
    total = int(img.headers.get('content-length', 0))
    with open(path + '//' + url_2.rsplit('/')[-1], 'wb')as f, tqdm(
        total=total,
        bar_format='进度:{percentage:3.0f}%|{bar}|'
    )as bar:
        for data in img.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)


if __name__ == '__main__':
    url = 'https://roco.qq.com/act/a20110727lkwg/wallpaper.shtml'
    img_list = analysis(url)
    pool = ThreadPoolExecutor(3)
    for key, value in img_list.items():
        for i in value:
            if not os.path.exists(key + '/' + i.rsplit('/')[-1]):
                pool.submit(down_img, key, i)
    pool.shutdown(wait=True)


