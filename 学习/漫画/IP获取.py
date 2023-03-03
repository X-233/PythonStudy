# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
import requests
from random import choice as ch
from lxml import etree
import redis

class IP:
    def __init__(self):
        self.Headers = [
            {
                'User-Agent': "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
            {
                'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
            {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"},
            {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"},
            {'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"},
            {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
            {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
            {'User-Agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"},
            {'User-Agent': "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"},
            {
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)"},
            {
                'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"},
            {
                'User-Agent': "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"},
            {
                'User-Agent': "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"},
            {
                'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"},
            {
                'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
            {
                'User-Agent': "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
            {
                'User-Agent': "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10"},
            {
                'User-Agent': "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13"},
            {
                'User-Agent': "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+"},
            {
                'User-Agent': "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0"},
            {
                'User-Agent': "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124"},
            {
                'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)"},
            {'User-Agent': "UCWEB7.0.2.37/28/999"},
            {'User-Agent': "NOKIA5700/ UCWEB7.0.2.37/28/999"},
            {'User-Agent': "Openwave/ UCWEB7.0.2.37/28/999"},
            {'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"},
            {
                'User-Agent': "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25"},
        ]
        self.list_IP = []

    def beesproxy(self, url):
        #获取总页数
        re1 = requests.get(url=url, headers=ch(self.Headers))
        text1 = re1.text
        xpath = etree.HTML(text1)
        quantity = xpath.xpath('//*[@id="free-second"]/div/div/div/div[2]/a[3]/text()')[0]
        # print(quantity)
        re1.close()
        #遍历url
        url = url.rsplit('/', 1)[0] + '/'
        # print(url)

        for i in range(int(quantity) + 1)[1:]:
            url1 = url + str(i)
            re2 = requests.get(url=url1, headers=ch(self.Headers))
            text1 = re2.text
            xpath = etree.HTML(text1)
            xpath1 = xpath.xpath('//*[@id="article-copyright"]/figure/table/tbody/tr')
            for j in xpath1:
                ip = j.xpath('./td[1]/text()')[0]
                port = j.xpath('./td[2]/text()')[0]
                # negotiate = j.xpath('./td[5]/text()')[0]
                # negotiate = str(negotiate).lower()
                self.list_IP.append(str(ip) + ':' + str(port))
                # self.list_IP.append('https' + '://' + str(ip) + ':' + str(port))
        r4 = Redis()
        for i in IPS.list_IP:
            r4.redis_4.sadd('IP_Best', i)
        r4.close()

class Redis:
    def __init__(self):
        self.redis_4 = redis.StrictRedis(host="180.76.187.206",
                                    port=6379,
                                    password="zhanglin",
                                    db=4,
                                    username="default")
        self.redis_4.delete('IP_Best')

    def close(self):
        self.redis_4.close()

if __name__ == '__main__':
    IPS = IP()
    IPS.beesproxy('https://www.beesproxy.com/free/page/1')


