# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
# src, file_type, output, strat, finish
import os
import re

#主路经
def path_analysis(path_1):
    str_1 = path_1
    names = os.listdir(str_1)
    # 排序有问题,得
    names.sort(key=lambda x: int(re.findall(r'第(\d+)话', x)[0]))
    return names

if __name__ == '__main__':
    str_1 = "/漫画/隔壁老王家"
    name = path_analysis(str_1)
    data = []
    for i in name:
        str_2 = i
        datanames = os.listdir(str_1 + '/' + str_2)
        # 排序有问题,得
        datanames.sort(key=lambda x: int(x[:-4]))
        data.append([str_1 + '/' + str_2 + '/', '.jpg', i + '.html', int(datanames[0][0:-4]), len(datanames)])

    pre = ''
    next = ''
    count = 0
    for d in data:
        src = d[0]
        file_type = d[1]
        output = d[2]
        if (count > 0):
            pre = data[count-1][2];
        if (count < len(data)-1):
            next = data[count+1][2];
        count += 1
        strat = d[3]
        finish = d[4]
        with open(output, 'w', encoding='utf-8') as f:
            f.write("<html><meta charset='UTF-8'><style>div {margin: auto;width: 900px;}img{width: 95%;} .pic {position: relative;} .pic span {position: absolute;bottom: 0;right: -2px;}</style><body><div>")
            for i in range(strat, finish):
                f.write("<div class='pic'><img src=\"" + src)
                f.write("%d" % i)
                f.write(file_type + "\"></div>")
                # f.write("%d" % i)
            f.write("<button><a href='"+ pre + "'>前一章 </a></button> <button><a href='"+ next +"'> 下一章</a></button>   </div><script>"
                    "window.onload = function(){"
                    "let index = 1;"
                    "let pic_div = document.querySelectorAll('.pic');"
                    "for (let i = 0; i<pic_div.length; i++) {"
                    "let span_ele = document.createElement('span');"
                    "span_ele.innerHTML = index++;"
                    "pic_div[i].appendChild(span_ele);"
                    "}"
                    "}"
                    ""
                    "</script></body></html>")
