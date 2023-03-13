"""
需要的结果如下
['201802', '201803', '201804', ..., '201912', '202001']

兴趣阅读:
在爬取东北三省包括黑龙江，吉林，辽宁三个省所有市县历史 2014年01月至2019年12月 的空气质量指数包括（AQI指数，空气质量状况，PM10，PM2.5，Co，No2，So2，O3）（http://www.tianqihoubao.com/）
分析：http://www.tianqihoubao.com/lishi/beijing.html
"""

import datetime
from dateutil.relativedelta import relativedelta  # 月份相对时间差模块
import requests

import parsel
import requests


def header():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    return headers


if __name__ == '__main__':
    url = 'http://www.tianqihoubao.com/lishi/beijing.html'
    html = requests.get(url=url, headers=header())
    select = parsel.Selector(html.text)
    print(html.status_code)
    select_1 = select.xpath('//div[@id="content"]')
    select_2 = select_1.xpath('.//div[@class="box pcity"]')

    for i in select_2:
        print(i.xpath('.//li').getall())