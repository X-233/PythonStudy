# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
import requests
from lxml import etree
from bs4 import BeautifulSoup

if __name__ == '__main__':
    text_str = """<html>
    	<head>
    		<title>测试bs4模块脚本</title>
    	</head>
    	<body>
    		<h1>橡皮擦的爬虫课</h1>
    		<p>用1段自定义的 HTML 代码来演示</p>
    		<p>用2段自定义的 HTML 代码来演示</p>
    		<a href="https://">wangzhan</a>
    	</body>
    </html>
    """

    # 实例化 Beautiful Soup 对象
    soup = BeautifulSoup(text_str, "html.parser")
    # 上述是将字符串格式化为 Beautiful Soup 对象，你可以从一个文件进行格式化
    # soup = BeautifulSoup(open('test.html'))

    print(soup.title.name)
    print(soup.body.p)
    print(soup.a.attrs)

