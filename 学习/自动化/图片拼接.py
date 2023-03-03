# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
# import certifi
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
#
# web = Chrome()
# web.get('https://www.ipingfang.cn/ol/pinjie.html')
#
# #定位元素
# web.find_element(By.NAME, "keyword").send_keys('风景')


import os
from PIL import Image
import cv2

# 定义输入的文件夹和输出的文件夹
dir = "E:\\download\\pengran\\"
sdir = "E:\\download\\xindong\\"
# 设置输出图像的宽度，当然也可以读取图像的
width = 750


# 合成图片，这里需要注意的是python读取列表的顺序是否和你想要的顺序是一样的
def creat_img(path, height, width, spath):
    suh = 0
    # suw = 0
    imgs = [Image.open(os.path.join(path, str(i) + ".jpg")) for i in range(len(os.listdir(path)))]
    result = Image.new(imgs[0].mode, (width, height))
    for i, img in enumerate(imgs):
        pic_path = os.path.join(path, str(i) + ".jpg")
        im = cv2.imread(pic_path)
        imh = im.shape[0]
        result.paste(img, box=(0, suh))
        suh += imh
    # result.show()
    result.save(spath)


# 获取要合并图片的总高度
def get_sunh(path):
    sum_h = 0
    dirlist = os.listdir(path)
    for i in dirlist:
        pic_path = os.path.join(path, i)
        img = cv2.imread(pic_path)
        img_h = img.shape[0]
        sum_h += img_h
    return sum_h


# 好像没用到
def createpath(path):
    flag = True
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    else:
        flag = False
    return flag


# 对于某个顺序，找到其类似的文件夹
def path_list(num):
    pl = []
    for i in range(1, 5):
        if i == 1:
            path = dir + str(num)
        else:
            path = dir + str(num) + "-" + str(i)
        if os.path.exists(path): pl.append(path)
    return pl


# 设置循环，分别合并图片
for i in range(1, 201):
    list = path_list(i)
    for j in list:
        name = j.split("\\")[-1]
        spath = os.path.join(sdir, str(name) + ".jpg")
        print(spath)
        height = get_sunh(j)
        creat_img(j, height, width, spath)


