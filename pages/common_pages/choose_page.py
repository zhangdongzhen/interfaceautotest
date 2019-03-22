# -*- coding: utf-8 -*-
import time
from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
from pages.common_pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChoosePage(BasePage):


    def click_menu_bt(self, button_pos):

        time.sleep(3)
        handleNow = self.driver.current_window_handle # 获得当前窗口
        self.driver.switch_to_window(handleNow)
        self.driver.implicitly_wait(3)
        # css_path = "#sortContainer > a:nth-child(" + str(button_pos) + ")" #把按钮位置设为参数获取
        if button_pos =='1':
            self.deprint("开始进入微信")
            button_id = 'module_1'

        # if button_pos =='2':
        #     self.deprint("开始进入H5制作")
        #
        #
        # if button_pos =='3':
        #     self.deprint("开始进入DSP投放（ADTIME）")
        #     button_id = 'module_5001'
        #
        # if button_pos =='4':
        #     self.deprint("开始进入SEM助手（九枝兰）")
        #     button_id = 'module_5002'
        #
        # if button_pos =='5':
        #     self.deprint("开始进入轨迹追踪")
        #
        # if button_pos =='6':
        #     self.deprint("开始进入数据监测工具")
        #     button_id = 'module_5004'
        #
        # if button_pos =='7':
        #     self.deprint("开始进入智能分析")
        #     button_id = 'module_5005'
        #
        # if button_pos =='8':
        #     self.deprint("开始进入数据看板")
        #     button_id = 'module_5007'

        if button_pos =='9':
            self.deprint("开始进入线上会")
            button_id = 'module_2'

        if button_pos =='10':
            self.deprint("开始进入线下会")
            button_id = 'module_3'

        if button_pos =='11':
            self.deprint("开始进入表单管理")
            button_id = 'module_7'

        if button_pos =='12':
            self.deprint("开始进入问卷")
            button_id = 'module_8'

        if button_pos == '13':
            self.deprint("开始进入抽奖")
            button_id = 'module_9'

        if button_pos == '14':
            self.deprint("开始进入投票")
            button_id = 'module_10'

        if button_pos == '15':
            self.deprint("开始进入微讨论")
            button_id = 'module_24'

        if button_pos == '16':
            self.deprint("开始进入产品管理")
            button_id = 'module_25'

        if button_pos == '17':
            self.deprint("开始进入客户管理")
            button_id = 'module_11'

        if button_pos == '18':
            self.deprint("开始进入文件管理")
            button_id = 'module_12'

        if button_pos == '19':
            self.deprint("开始进入供应商管理")
            button_id = 'module_13'

        if button_pos == '20':
            self.deprint("开始进入邮件管理")
            button_id = 'module_16'

        if button_pos == '21':
            self.deprint("开始进入短信管理")
            button_id = 'module_17'

        if button_pos == '22':
            self.deprint("开始进入文章管理")
            button_id = 'module_26'

        if button_pos == '23':
            self.deprint("开始进入账号")
            button_id = 'module_18'

        if button_pos == '24':
            self.deprint("开始进入角色管理")
            button_id = 'module_19'

        if button_pos == '25':
            self.deprint("开始进入模块管理")


        if button_pos == '26':
            self.deprint("开始进入字典表管理")
            button_id = 'module_27'

        self.wait_is_visible('id', button_id)
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[-1]) # 获取下一个窗口句柄，跳转
        return handleNow
if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('1')
    # o.quit()