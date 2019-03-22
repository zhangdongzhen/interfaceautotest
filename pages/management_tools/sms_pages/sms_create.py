# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower


class SmsCreatePage(BasePage):

    #创建一个全局的短信任务
    def create_sms(self,type):
        time.sleep(8)
        self.deprint("点击右键任务管理的新建任务按钮")
        self.wait_is_visible('x','/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/button') #点击新建任务按钮
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[1]/div/input',u'自动化创建' + self.nowtime())#输入任务名称
        self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/div/button/span[2]')#点击任务分类
        if type=="邀请短信":
            self.wait_is_visible('x', '//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/div/ul/li[1]')
        if type=="感谢短信":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/div/ul/li[2]')
        if type=="通知短信":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/div/ul/li[3]')
        if type=="报名确认短信":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/div/ul/li[4]')
        if type=="审核通过通知短信":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/div/ul/li[5]')
        if type == "审核不通过通知短信":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/div/ul/li[6]')
        if type=="其他":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/div/ul/li[7]')
        time.sleep(3)
        try:
            self.wait_is_visible('x', '//*[@id="createTask"]/div/div/div[3]/button[2]')  # 点击确定按钮
            return u'短信创建成功'
        except:
            return u'短信创建失败'

    #点击第一个短信任务
    def list_sms(self):#20180809
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        self.wait_is_visible('x','/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a[1]') #点击第一个短信任务


if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('21')
    type="邀请短信"
    s=SmsCreatePage(dr)
    s.create_sms(type)
    s.list_sms()



