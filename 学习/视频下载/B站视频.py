# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰

from concurrent.futures import ThreadPoolExecutor
import requests
import re
from random import choice
import json
import os
import subprocess
from lxml import etree
import redis

word = input('请输入要下载视频的网址:\n')

H = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
     'Referer': word,
     'cookie': "DedeUserID=514671750; DedeUserID__ckMd5=9b4aa2e41166602b; CURRENT_BLACKGAP=0; buvid3=FCDDE561-34C0-2BCC-8A02-78758A5609FB14015infoc; b_nut=1668947014; LIVE_BUVID=AUTO4716689470365564; _uuid=6A24B57A-4586-61B1-846A-ED6772A11087A54400infoc; buvid_fp_plain=undefined; SESSDATA=b2c52ae8%2C1684499612%2C56e16%2Ab1; bili_jct=8501ee48b708edbfe86f9242bf3ab323; i-wanna-go-back=-1; b_ut=5; rpdid=|(J|YJJulJmR0J'uYYm|kmRuu; nostalgia_conf=-1; buvid4=CA42D156-3364-4871-EA54-E625E81C51F914015-022112020-TNlJn%2By0Jb0TgG7rSqJNrw%3D%3D; is-2022-channel=1; CURRENT_FNVAL=4048; fingerprint=3247e668c7cf521317162735e2e6625a; header_theme_version=CLOSE; hit-new-style-dyn=0; hit-dyn-v2=1; CURRENT_QUALITY=80; bp_video_offset_514671750=765734309093966000; sid=5ded7qgo; PVID=3; buvid_fp=f20a3125ba5b9ccfa12d2ce5eede2a37; b_lsid=51C55833_1867D21B741; innersign=1",
    },
]

if not os.path.exists('video'):
    os.mkdir('video')


def Analysis_start():
    url = word
    text_s = requests.get(url=url, headers=choice(H))

    text_s = text_s.text
    # str_1 = (re.findall('<span class="cur-page">(.*?)</span>', text_s, re.S))[0]
    html = etree.HTML(text_s)
    title = html.xpath('//*[@id="viewbox_report"]/h1/@title')[0]

    str_2 = (re.findall('<script>window.__INITIAL_STATE__=(.*?)</script>', text_s, re.S))[0]
    str_3 = re.findall('(.*?);\\(function\\(\\)', str_2)[0]
    # print(str_3)

    json_2 = json.loads(str_3)
    # pprint.pprint(json_2)
    #
    # with open('1.json', 'w', encoding='utf-8')as f:
    #     f.write(str(json_2))

    item = {}
    Inf = json_2['videoData']['pages']
    for i in Inf:
        part = re.sub('[\d+]', '', i['part'])
        part = re.sub(' ', '', part)
        #strip是把空格删除,方便后面文件读写
        item[str(i['page']) + '_' + (str(part).strip())] = word + '?p=' + str(i['page'])
    print(item)

    return item, str(title).replace(' ', '_')

def Analysis(text_1, url, text_3):
    text = requests.get(url=url, headers=choice(H), timeout=10)
    # f = open('1.html', 'w', encoding='utf-8')
    # f.write(text.text)
    # f.close()
    # text_1 = (re.findall('class="video-title tit">(.*?)</h1>', text.text, re.S))[0]
    #找到包含视频网址的数据
    text_2 = re.findall('<script>window.__playinfo__=(.*?)</script>', text.text, re.S)
    # print(text_1[0])
    # print(json.loads(text_2[0]))
    json_1 = json.loads(text_2[0])

    # pprint.pprint(json_1)
    str_1 = json_1['data']['dash']['audio'][0]['baseUrl']
    str_2 = json_1['data']['dash']['video'][0]['baseUrl']
    # print(str_1)
    # print(str_2)
    print('正在下载......')
    re_1 = requests.get(url=str_1, headers=choice(H)).content
    re_2 = requests.get(url=str_2, headers=choice(H)).content

    if not os.path.exists(f'D:\\视频\\爬虫\\{text_3}'):
        os.mkdir(f'D:\\视频\\爬虫\\{text_3}')

    with open('video\\' + text_1 + '.mp3', mode='wb')as f_1:
        f_1.write(re_1)
    with open('video\\' + text_1 + '.mp4', mode='wb')as f_2:
        f_2.write(re_2)

    print('下载完成\t' + text_1)

    print('正在合成')
    if os.path.exists(f'video\\{text_1}.mp4'):
        # 'https://www.bilibili.com/video/BV1t94y1f7Ex'
        # 'https://www.bilibili.com/video/BV15F411s7Qd'
        COMMAND = f'D:\\FFmpeg\\bin\\ffmpeg.exe -i video\\{text_1}.mp3 -i video\\{text_1}.mp4 -codec copy D:\\视频\\爬虫\\{text_3}\\{text_1}.mp4'
        # COMMAND = f'D:\\FFmpeg\\bin\\ffmpeg.exe -i video\\{text_1}.mp3 -i video\\{text_1}.mp4 -c:v copy -c:a acc -strict experimental video_1\\{text_1}output.mp4'
        subprocess.run(COMMAND, shell=True, encoding='gbk', stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        # , stdout = subprocess.PIPE, stderr = subprocess.STDOUT


if __name__ == '__main__':
    pool = ThreadPoolExecutor(3)
    list_url, title = Analysis_start()
    for key, value in list_url.items():
        if not os.path.exists(f'D:\\视频\\爬虫\\{title}\\{key}.mp4'):
            pool.submit(Analysis, key, value, title)
            # print(key)
    pool.shutdown(wait=True)
    if os.path.exists('video'):
        COMMAND2 = f'rd /s/q video'
        subprocess.run(COMMAND2, shell=True, encoding='utf-8')
