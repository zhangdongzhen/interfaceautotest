# -*- coding: utf-8 -*-

import time
from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
import random


class FrontLogin(BasePage):

    def login(self,username,password):

        self.deprint('进入登录页面')
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 跳转到登录页面
        #输入手机号
        self.element_value_input('x', '//*[@name="zhanghao"]', username)
        #输入密码
        self.element_value_input('x', '//*[@name="mima"]', password)
        time.sleep(2)
        self.element_click('x', '//*[@id="con_one_1"]/input')  # 点击登录按钮
        self.deprint('登录成功')




if __name__ == '__main__':
        dr = brower()
        # o = LoginPage(dr)
        # o.login()
        # o = ChoosePage(dr)
        # time.sleep(3)
        # o.click_menu_bt('9')
        # o = IndexPage(dr)#调用线下会的类
        # o.click_createunderline()#调用线下会点击首页的创建会议按钮的方法
        # o = NewMeetingPage(dr)#调用线下会的类
        # o.create_neww_offline()#调用线下会创建会议的方法
        # # S = Edm_offline(dr)
        # S.createofflineEdm()
        # S.startsigning()
        # S.signupoffline()



