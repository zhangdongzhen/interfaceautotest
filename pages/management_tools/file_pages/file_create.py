# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower


class Create_File(BasePage):

    def create_file(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        time.sleep(3)
        self.wait_is_visible('x','/html/body/div/div[1]/div[2]/div[4]/div[2]/div/button[3]')#点击新建文件夹按钮
        self.element_value_input('x','//*[@id="downloadList"]/div/div[2]/div[1]/div[1]/div/input',u'自动化创建文件夹' + self.nowtime())#输入文件夹名称
        # pyautogui.dragTo(left)
        self.wait_is_visible('x','//*[@id="downloadList"]/div/div[2]/div[2]/div/div[1]/div')#点击限制文件类型的按钮
        self.element_value_input('x', '//*[@id="downloadList"]/div/div[2]/div[2]/div/div[2]/input',u'xlsx')  # 输入文件类型
        self.wait_is_visible('x', '//*[@id="downloadList"]/div/div[2]/div[3]/div/div/div/span[2]')  # 点击第三方上传，选择需要审核
        self.wait_is_visible('x', '//*[@id="downloadList"]/div/div[2]/div[3]/div/label/ins')  #选择需要审核
        self.wait_is_visible('x', '//*[@id="downloadList"]/div/div[2]/div[4]/div/label/ins')  # 点击允许共享按钮
        self.wait_is_visible('x', '//*[@id="downloadList"]/div/div[2]/div[5]/div/label[1]/ins')  # 点击允许共享按钮
        self.scrollbar('bottom')
        time.sleep(2)
        self.wait_is_visible('x','//*[@id="downloadList"]/div/div[2]/div[8]/button')#点击保存按钮









if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('18')
    S = Create_File(dr)
    S.create_file()
