# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰

import requests
from random import choice
import re
import os

def get_headers():
    uas = [
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
        "Baiduspider-image+(+http://www.baidu.com/search/spider.htm)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 YisouSpider/5.0 Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; Googlebot-Image/1.0; +http://www.google.com/bot.html)",
        "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Sogou News Spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Sosospider+(+http://help.soso.com/webspider.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)"
    ]
    ua = choice(uas)
    headers = {
        "user-agent": ua,
        "referer": "https://www.baidu.com"
    }
    return headers

def Anasisy(text):
    # html = re.findall('window.__NUXT__=(.*?)</script>', text)[0]
    html = re.findall('charList:(.*?),mod3Index', text)[0]
    # html = re.findall('\[(.*)\]', html)[0]
    #数据里面是用的双引号, 取出来最外层也是双引号,得换成单引号
    # html = '\'' + html + '\''
    title = re.compile('title:"(.*?)"')
    icon = re.compile('icon:"(.*?)"')
    cover1 = re.compile('cover1:"(.*?)"')
    cover2 = re.compile('cover2:"(.*?)"')
    cv_cn = re.compile('cv:\[\{name:"(.*?)",audio:\[(.*?)]},\{name:"(.*?)",audio:\[(.*?)]}')
    cv = cv_cn.findall(html)
    title = title.findall(html)
    icon = icon.findall(html)
    cover1 = cover1.findall(html)
    cover2 = cover2.findall(html)
    for i in range(len(title)):
        dict_list = {
            "title": title[i],
            "icon": icon[i],
            "cover1": cover1[i],
            "cover2": cover2[i],
            "cv_cn_name": cv[i][0],
            "cv_jp_name": cv[i][2],
            "cv_cn": cv[i][1].split(','),
            "cv_jp": cv[i][3].split(','),
        }

        Save(dict_list)

def Save(dict_list):
    path = os.path.exists('D:/爬虫/原神')
    #判断是否有该文件夹
    if not path:
        os.mkdir('D:/爬虫/原神')

    title = dict_list["title"]
    icon = dict_list["icon"]
    cover1 = dict_list["cover1"]
    cover2 = dict_list["cover2"]
    cv_cn_name = dict_list["cv_cn_name"]
    cv_jp_name = dict_list["cv_jp_name"]
    cv_cn = dict_list["cv_cn"]
    cv_jp = dict_list["cv_jp"]
    if not os.path.exists(f'D:/爬虫/原神/{title}/'):
        os.mkdir(f'D:/爬虫/原神/{title}/')

    #保存图片
    Save_images(title, icon, cover1, cover2)
    #保存配音
    Save_autios(title, cv_cn_name, cv_jp_name, cv_cn, cv_jp)

def Save_images(title, icon, cover1, cover2):
    if not os.path.exists(f'D:/爬虫/原神/{title}/icon.png'):
        # 转义
        icon = icon.encode('utf-8').decode('unicode-escape')
        re1 = requests.get(url=icon, headers=get_headers(), timeout=7).content
        with open(f'D:/爬虫/原神/{title}/icon.png', 'wb') as f:
            f.write(re1)
    if not os.path.exists(f'D:/爬虫/原神/{title}/cov1.png'):
        # 转义
        cover1 = cover1.encode('utf-8').decode('unicode-escape')
        re2 = requests.get(url=cover1, headers=get_headers(), timeout=7).content
        with open(f'D:/爬虫/原神/{title}/cov1.png', 'wb') as f1:
            f1.write(re2)
    if not os.path.exists(f'D:/爬虫/原神/{title}/cov2.png'):
        # 转义
        cover2 = cover2.encode('utf-8').decode('unicode-escape')
        re3 = requests.get(url=cover2, headers=get_headers(), timeout=7).content
        with open(f'D:/爬虫/原神/{title}/cov2.png', 'wb') as f2:
            f2.write(re3)

def Save_autios(title, cv_cn_name, cv_jp_name, cv_cn, cv_jp):
    # for i in cv_cn:
    #
    # for i in cv_jp:
    pass
def Run(url):
    text = requests.get(url=url, headers=get_headers(), timeout=7).text
    Anasisy(text)

if __name__ == '__main__':
    url = 'https://ys.mihoyo.com/main/character/mondstadt'
    Run(url)

