# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from lxml import etree
import time

def Header():
    headers = {
        'Cookie': 'pgv_pvid=4619374500; RK=7knNeePRSf; ptcz=01821b5616eb455ddfca915c454a4acaff3b08fa4c00fc62ef54d78fce7fdb25; fqm_pvqid=8b59ac24-0290-48a9-af41-fbf4f4827e11; fqm_sessionid=41a24209-a326-4dcd-9e48-91c39f100454; pgv_info=ssid=s4701823217; ts_uid=5622696588; ts_last=y.qq.com/n/ryqq/toplist/4; ts_refer=i.y.qq.com/',
        'Referer': 'https://i.y.qq.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'origin': 'https://y.qq.com'
    }
    return headers


def Data():
    data = {
        "comm": {"cv": 4747474, "ct": 24, "format": "json", "inCharset": "utf-8", "outCharset": "utf-8", "notice": 0,
                 "platform": "yqq.json", "needNewCode": 1, "uin": 0, "g_tk_new_20200303": 2006525704,
                 "g_tk": 2006525704},
        "req_1": {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey",
                  "param": {"guid": "5620931744", "songmid": ["001TcTRO1D803d"], "songtype": [0], "uin": "0",
                            "loginflag": 1, "platform": "20"}}
    }
    return data


if __name__ == '__main__':
    purl = 'RS02064dfdIM38rSZY.mp3?guid=4314806824&vkey=22DDC4471DA656B52606E9B67111AF1C54A4E31988479A50114E4E9B5D8D0F7A7828122408920AFEBA9F5E6E0A56D166BFE244910DDCAAE2&uin=1972125134&fromtag=120052'
    url = 'https://dl.stream.qqmusic.qq.com/' + purl

    data = Data()
    time_1 = int(time.time()*1000)
    print(time_1)
    # sign =
    url_1 = f'https://u.y.qq.com/cgi-bin/musics.fcg?'
    headers = Header()
    '1671864814878'
    '1671864814131'
    html = requests.post(url=url_1, headers=headers, params=data)
    print(html.json())
