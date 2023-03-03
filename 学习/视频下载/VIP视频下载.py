# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
import requests

def Analysis():
    data = {"duration":{"fetch":[],"static":[{"url":"https://puui.qpic.cn/video_caps/0/e0045h8phxs.q3.3.jpg/0","method":"get","duration":596.7,"status":200,"type":"static","isHttps":True,"nextHopProtocol":"h2","urlQuery":"","domainLookup":0,"connectTime":0}],"bridge":[]},"id":"nGL3ESKDmLpkbOP45x","uin":"23ab1a832afff0ba","version":"1.0.2.9712rc_ci_202212130212","aid":"43413fb4-6718-400a-973f-0351af281dbb","env":"production","ext1":"23ab1a832afff0ba_null","ext2":"web_formal","platform":3,"netType":4,"vp":"1440 * 809","sr":"1440 * 960","sessionId":"session-1671000855836","from":"https://v.qq.com/x/cover/mzc00200pzl5rvb/l0045z5d3s0.html","referer":"https://v.qq.com/channel/choice?channel_2022=1"}
    header = {
        'referer': 'https://v.qq.com/',
        'origin': 'https://v.qq.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    url = 'https://aegis.qq.com/speed?id=nGL3ESKDmLpkbOP45x&uin=23ab1a832afff0ba&version=1.0.2.9712rc_ci_202212130212&aid=43413fb4-6718-400a-973f-0351af281dbb&env=production&ext1=23ab1a832afff0ba_null&ext2=web_formal&platform=3&netType=4&vp=1440%20*%20809&sr=1440%20*%20960&sessionId=session-1671000855836&from=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200pzl5rvb%2Fl0045z5d3s0.html&referer=https%3A%2F%2Fv.qq.com%2Fchannel%2Fchoice%3Fchannel_2022%3D1'

    re1 = requests.post(url=url, headers=header, data=data)
    print(re1.text)
    mp4 = re1.content
    with open('1.mp4', 'wb')as f:
        f.write(mp4)
if __name__ == '__main__':
    Analysis()
