# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰

###############自动打卡

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#键盘操作
from selenium.webdriver.common.keys import Keys
from time import sleep
#下拉select,css动态加载出来的
from selenium.webdriver.support.select import Select
from random import choice

url = 'http://login.cuit.edu.cn/Login/xLogin/Login.asp'

list_results = ['剪头发', '实习', '面试', '吃饭']

def Daka(user, pwd):
    # 记得加()
    web = Chrome()
    web.get(url=url)
    web.find_element(By.XPATH, '//*[@id="txtId"]').send_keys(user)

    web.find_element(By.XPATH, '//*[@id="txtMM"]').send_keys(pwd)

    sleep(2)
    web.find_element(By.XPATH, '//*[@id="IbtnEnter"]').click()
    sleep(2)
    web.find_element(By.XPATH, '//tbody[2]/tr[2]/td[2]/a[@target="_self"]').click()
    sleep(2)
    # 无新型冠状病毒感染症状
    web.find_element(By.XPATH, '//input[@name="sF21932_1"]').click()
    sleep(2)
    # 目的地
    web.find_element(By.XPATH, '//input[@name="sF21912_1"]').send_keys('成都')
    sleep(2)
    # 事情缘由
    web.find_element(By.XPATH, '//input[@name="sF21912_2"]').send_keys(choice(list_results))
    sleep(2)

    # 时间
    sel_1 = web.find_element(By.XPATH, '//select[@name="sF21912_3"]')
    sel_2 = Select(sel_1)
    sel_2.select_by_visible_text('今天')

    sel_1 = web.find_element(By.XPATH, '//select[@name="sF21912_4"]')
    sel_2 = Select(sel_1)
    sel_2.select_by_visible_text('10:00')

    sleep(2)
    sel_1 = web.find_element(By.XPATH, '//select[@name="sF21912_5"]')
    sel_2 = Select(sel_1)
    sel_2.select_by_visible_text('第2天')

    sel_1 = web.find_element(By.XPATH, '//select[@name="sF21912_6"]')
    sel_2 = Select(sel_1)
    sel_2.select_by_visible_text('10:00')

    # 提交
    web.find_element(By.XPATH, '//input[@name="B2"]').click()
    # sleep(1)
    # # 定位下拉列表
    # sel = web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[4]/td[2]/div/select[3]')
    # sel_1 = Select(sel)
    # # sel_2 = sel_1.options
    # sel_1.select_by_visible_text('在校外完成实习任务')
    #
    # sel = web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[4]/td[2]/div/select[4]')
    # sel_1 = Select(sel)
    # # sel_2 = sel_1.options
    # sel_1.select_by_visible_text('正常')
    #
    # sel = web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[4]/td[2]/div/select[5]')
    # sel_1 = Select(sel)
    # # sel_2 = sel_1.options
    # sel_1.select_by_visible_text('正常')
    #
    # sel = web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[4]/td[2]/div/select[6]')
    # sel_1 = Select(sel)
    # # sel_2 = sel_1.options
    # sel_1.select_by_visible_text('全部正常')
    #
    # # 出校
    # sel = web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[5]/td[2]/div/select[1]')
    # sel_1 = Select(sel)
    # # sel_2 = sel_1.options
    # sel_1.select_by_visible_text('明天')
    #
    # sel = web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[5]/td[2]/div/select[2]')
    # sel_1 = Select(sel)
    # # sel_2 = sel_1.options
    # sel_1.select_by_visible_text('06:00')
    #
    # # 出校
    # sel = web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[5]/td[2]/div/select[3]')
    # sel_1 = Select(sel)
    # # sel_2 = sel_1.options
    # sel_1.select_by_visible_text('第2天')
    #
    # sel = web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[5]/td[2]/div/select[4]')
    # sel_1 = Select(sel)
    # # sel_2 = sel_1.options
    # sel_1.select_by_visible_text('20:00')
    #
    # web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[5]/td[2]/div/input[1]').clear()
    # web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[5]/td[2]/div/input[1]').send_keys('武侯区环球中心')
    # web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[5]/td[2]/div/input[2]').clear()
    # web.find_element(By.XPATH, '//*[@id="wjTA"]/tbody/tr[5]/td[2]/div/input[2]').send_keys('实习')
    #
    # web.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr/td[1]/input').click()

    #浏览器调整选项
    sleep(1)
    alert = web.switch_to.alert
    alert.accept()

    sleep(2)
    web.close()

if __name__ == '__main__':
    Daka('2019021097', '11111111a')
    sleep(5)
    # Daka('2019042068', 'LSL280553a')
#窗口切换,新窗口默认不切换
# web.switch_to.window(web.window_handles[-1])#最后一个
# web.close()
#要拿iframe中内容,要切换到iframe视角
# iframe = web.find_element(By.XPATH, 'iframeXPATH地址')
# web.switch_to.frame(iframe)
#切换默认界面
# web.switch_to.default_content()





