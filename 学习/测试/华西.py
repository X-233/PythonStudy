# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import parsel
import requests


def header():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    return headers


if __name__ == '__main__':
    url = 'https://www.wchscu.cn/public/index.html'
    html = requests.get(url=url, headers=header())
    select = parsel.Selector(html.text)

    list_1 = select.xpath('//div[@class="slick-item"]')
    for i in list_1:
        main_title = i.xpath('.//div[@class="inner"]/div[1]/text()').get().strip()
        sub_title = i.xpath('.//div[@class="inner"]/div[2]/text()').get().strip()
        url_title = 'https://www.wchscu.cn' + i.xpath('.//div[@class="img"]/@style').re('\((.*?)\)')[0]
        print(main_title)
        print(sub_title)
        print(url_title)

