# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os
from time import sleep
import requests
import re

#主路经
def path_analysis(path_1):
    str_1 = path_1
    names = os.listdir(str_1)
    # 排序有问题,得
    names.sort(key=lambda x: int(re.findall(r'第(\d+)话', x)[0]))
    return names

#子路径
def path_analysis_2(path_2, i_img):
    str_1 = path_2 + '\\'
    datanames = os.listdir(str_1)
    # 排序有问题,得
    datanames.sort(key=lambda x: int(x[:-4]))
    if len(datanames) >= 20:
        m = 0
        for j in range(len(datanames) // 20 + 1):
            for i in datanames[j * 20: (j + 1) * 20]:
                print(i)
                web.find_element(By.XPATH, '//*[@id="newFile"]').send_keys(str_1 + i)
            web.find_element(By.XPATH, '//*[@id="ctl00_content_cmdSaveAttachment"]').click()
            img_url = web.find_element(By.XPATH, '//*[@id="ctl00_content_lblNew"]/a[2]').get_attribute('href')
            print(img_url)
            down_img(str(m), img_url, i_img)
            m += 1
            sleep(2)
        path_analysis_2(f'D:\\Pycharm\\FBS\\学习\\漫画\\{i_img}_1', i_img)
    else:
        for i in datanames:
            print(i)
            web.find_element(By.XPATH, '//*[@id="newFile"]').send_keys(str_1 + i)
        web.find_element(By.XPATH, '//*[@id="ctl00_content_cmdSaveAttachment"]').click()
        img_url = web.find_element(By.XPATH, '//*[@id="ctl00_content_lblNew"]/a[2]').get_attribute('href')
        print(img_url)
        down_img_1(0, img_url, i_img)
        sleep(2)
        # for i in datanames:
        #     os.remove(str_1 + i)
        # os.removedirs(str_1)

def down_img(m, img_url, i_img):
    re1 = requests.get(url=img_url, timeout=10).content
    if not os.path.exists(f'D:\\Pycharm\\FBS\\学习\\漫画\\{i_img}_1'):
        os.mkdir(f'D:\\Pycharm\\FBS\\学习\\漫画\\{i_img}_1')
    with open(f'D:\\Pycharm\\FBS\\学习\\漫画\\{i_img}_1\\' + m + '.png', 'wb')as f:
        f.write(re1)
        f.flush()
        f.close()

def down_img_1(m, img_url, i_img):
    re1 = requests.get(url=img_url, timeout=None).content
    if not os.path.exists(f'D:\\Pycharm\\FBS\\学习\\漫画\\{i_img}'):
        os.mkdir(f'D:\\Pycharm\\FBS\\学习\\漫画\\{i_img}')
    with open(f'D:\\Pycharm\\FBS\\学习\\漫画\\{i_img}\\' + str(m) + '.png', 'wb')as f:
        f.write(re1)
        f.flush()
        f.close()

if __name__ == '__main__':
    web = Chrome()
    web.get('http://www.zuohaotu.com/image-merge.aspx')
    path_all = 'D:\\Pycharm\\FBS\\学习\\漫画\\圣墟\\'
    names_all = path_analysis(path_all)
    for i in names_all:
        path_analysis_2(path_all + i, i)
        sleep(5)
    web.quit()
