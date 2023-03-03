# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化
# 3、公民个人信息不要去碰
import requests
from tkinter import *
import hashlib
import time
from random import randint
import pyperclip


def headers():
    header = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=211376722@10.112.57.88; OUTFOX_SEARCH_USER_ID_NCOO=1107887279.5379586; ___rl__test__cookies=1669778336524',
        'Host': 'fanyi.youdao.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'https://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    return header
def analysis():
    text_4 = 'i=hello&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=16697783365253&sign=1e1b33891c68d56867a8c44aae8dc663&lts=1669778336525&bv=9edd1e630b7d8f13679a536d504f3d9f&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_CLICKBUTTION'
    data_dict = {i.split('=')[0]: i.split('=')[-1] for i in text_4.split('&')}
    return data_dict
def run(event=None):
    word = Input.get('1.0', END)
    data_dict = analysis()
    header = headers()
    data_dict['i'] = word
    bv = hashlib.md5(header['User-Agent'].encode('utf-8')).hexdigest()
    ts = str(int(time.time() * 1000))
    salt = ts + str(randint(0, 10))
    md5 = 'fanyideskweb' + word + salt + 'Ygy_4c=r#e#4EX^NUGUc5'
    sign = hashlib.md5(md5.encode('utf-8')).hexdigest()
    data_dict['lts'] = ts
    data_dict['salt'] = salt
    data_dict['sign'] = sign
    data_dict['bv'] = bv
    try:
        html = requests.post(url='https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule',
                             headers=header,
                             data=data_dict).json()
        text_3.delete('1.0', END)
        text_4 = html['translateResult']
        text_1 = ''
        for i in text_4:
            if len(i) > 1:
                for j in i:
                    text_1 += j['tgt']
            else:
                text_1 += i[0]['tgt']

        text_3.insert(INSERT, text_1)
        pyperclip.copy(text_1)
    except Exception as e:
        text_3.delete('1.0', END)
        text_3.insert(INSERT, e)

def print_1(event=None):
    print('wancheng')

if __name__ == '__main__':

    root = Tk()
    root.title('翻译')
    W = root.winfo_screenwidth()
    H = root.winfo_screenheight()
    W1 = int(W*0.26)
    H1 = int(H*0.24)
    geometry = f'{W1}x{H1}'

    # 设置大小及其位置
    root.geometry(geometry)  # 2160x1440
    # 置顶
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.minsize(W1, H1)
    root.maxsize(2*W1, 2*H)
    # 透明°
    root.attributes("-alpha", 0.8)

    # Entry, 不要把grid加在后面,先生成对象,后面再定位置
    Input = Text(root, bd=1, height=2, wrap='char', undo=True, bg='#CCFFFF')
    # 翻译
    try:
        str_1 = pyperclip.paste()
        if str_1 != 'pyperclip.paste()':
            if isinstance(str_1, str):
                Input.insert(INSERT, str_1)
    except Exception as e:
        pass
    Input.grid(row=0, column=0, columnspan=5, sticky='nsew')
    # text
    text_3 = Text(root, font=('楷体_GB2312', '18'), wrap='word', undo=True, bg='#FFFFCC')
    text_3.insert(INSERT, '快捷键Alt + q: 翻译\n快捷键Alt + w: 关闭程序\n')
    text_3.grid(row=1, column=0, columnspan=6, sticky='nsew')
    # 锁定宽高
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure((1, 1), weight=1)
    # root.grid_columnconfigure(0, weight=1)
    # root.grid_rowconfigure(0, weight=1)
    # 按钮
    but = Button(root, text='翻译', command=lambda : run(), font=('楷体_GB2312', '20'), bg='#CC9999', fg='#FF33FF', bd=1)
    but.grid(row=0, column=5, sticky='se')
    but_2 = Button(root, font=('楷体_GB2312', '14'), command=lambda : root.destroy(), bd=0, text='✘', bg='#FFFFCC', fg='#FF33FF', cursor='arrow')
    but_2.grid(row=1, column=5, sticky='se')
    root.bind('<Alt-q>', run)
    root.bind('<Alt-w>', lambda event: root.destroy())
    root.mainloop()


