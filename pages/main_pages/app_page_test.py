# -*- coding: utf-8 -*-
import time
from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
from pages.common_pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
class AppPageTest(BasePage):

    #测试每个app是否正常进入主页面
    def click_menu_bt(self, button_pos,elementpath,validatename):
        winHandles = self.driver.window_handles
        # for handle in winHandles:
        #     print u"开始循环时句柄" + handle
        # time.sleep(3)
        # handleNow = self.driver.current_window_handle  # 获得当前窗口
        # print u"当前句柄" + handleNow
        # self.driver.switch_to_window(handleNow)
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[0])
        # self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(40)
        self.driver.maximize_window()
        try:
            # css_path = "#sortContainer > a:nth-child(" + str(button_pos) + ")"  # 把按钮位置设为参数获取
            # self.wait_is_visible('css', css_path)  #点击应用按钮
            self.click_menu(button_pos)
        except Exception:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.close()
            return int(0)


        # time.sleep(3)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        flag = 0
        try:
            # print self.driver.window_handles[-1]
            self.driver.switch_to.window(self.driver.window_handles[-1])
            #获取应用页面的数据统计元素
            r = 0
            for m in range(0,120):
                elem = self.find_element_text('x', elementpath)
                # elem = self.find_element_text('x', '//*[@id="g-right"]/section/div/div[2]/div[1]')
                # time.sleep(10)
                self.deprint(u"测试应用：" + elem)
                if elem.replace(' ','') != '' and elem .replace(' ','') == validatename:
                    # 访问成功
                    self.close()
                    result = 1
                    break

                elif elem.replace(' ','') != '' and elem .replace(' ','') != validatename:
                    # 访问失败
                    self.close()
                    result = 0
                    break
                else :
                    time.sleep(0.5)
                    r = r+1
            if r == 120 :
                # if button_pos != 26 :
                self.close()
                result = 0
            return result
        except Exception:
            # self.driver.switch_to.window(self.driver.window_handles[-1])
            self.close()
            result = 0
            return result


    #循环遍历每个应用
    def cyclic_test_app(self,num):
        actual_result = 2
        actual_dict = {}
        n = 1
        while n < num:
            #DSP投放\SEM助手\轨迹追踪\数据监测暂不监控，模块管理新首页去了该功能
            if n == 3 or n == 4 or n == 6 or n == 25  or n == 5 :
                n = n + 1
                continue
            elif n == 1 :
                elepath = '//*[@id="g-right"]/section/div/div[1]/div[1]/div/div[1]/span'
                name = u'新消息'
            elif n == 2 :
                elepath = '//*[@id="main"]/div[2]/div/div[2]/ul/li[1]/div/p[1]'
                name = '1'
            # elif n == 5 :
            #     elepath = '/html/body/div[1]/header/div/div/div[2]/div/div/span'
            #     name = u'sinobaseApp用户'
            elif n == 7 :
                elepath = '//*[@id="TenantName"]'
                name = u'内部_产品_UI自动化组'
            elif n == 8 :
                elepath = '//*[@id="userName"]/span'
                name = u'内部_产品_UI自动化组张站平'
            elif n == 9 :
                elepath = '//*[@id="collapse5"]/li[3]/a'
                name = u'数据权限设置'
            elif n == 10 :
                elepath = '/html/body/div[2]/nav/div/ul/li[1]/a/span'
                name = u'首页'
            elif n == 11 :
                elepath = '/html/body/div[2]/div[1]/main/div[1]/div[1]/div[2]/button'
                name = u'新建表单'
            elif n == 12 :
                elepath = '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/div[2]/a/span'
                name = u'新建问卷'
            elif n == 13 :
                elepath = '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div/span/button'
                name = u'搜索'
            elif n == 14 :
                elepath = '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/button/span'
                name = u'新建投票'
            elif n == 15 :
                elepath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/button'
                name = u'新建论坛'
            elif n == 16 :
                elepath = '/html/body/div[1]/section/div[1]/div[1]/div/button'
                name = u'新建产品线'
            elif n == 17 :
                elepath = '/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[1]/a'
                name = u'复合筛选'
            elif n == 18 :
                elepath = '/html/body/div/div[1]/div[2]/div[4]/div[2]/div/button[1]'
                name = u'上传文件'
                # elepath = '/html/body/div/div[1]/header/div[2]/div/div/div/button/span[3]'
                # name = u'内部_产品_UI自动化组'
            elif n == 19 :
                elepath = '/html/body/div[2]/div[2]/div[1]/a'
                name = u'创建新供应商'
            elif n == 20 :
                elepath = '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/button'
                name = u'新建任务'
            elif n == 21 :
                elepath = '/html/body/div[1]/div[3]/div[1]/div[1]'
                name = u'短信列表'
            elif n == 22 :
                elepath = '/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/a'
                name = u'新建栏目'
            elif n == 23 :
                elepath = '/html/body/div[2]/div[2]/div[1]/a'
                name = u'创建新用户'
            elif n == 24 :
                elepath = '/html/body/div[2]/div[2]/div[2]/a'
                name = u'新增全局角色'
            # elif n == 25 :
            #     elepath = '/html/body/div[2]/div[2]/div[1]/h2'
            #     name = u'模块管理'
            elif n == 26 :
                elepath = '//*[@id="g-right"]/div/div[1]/h2'
                name = u'全局字典表管理'
            actual_result=self.click_menu_bt(str(n),elepath,name)
            if actual_result == 0 :
                self.driver.switch_to.window(self.driver.window_handles[0])
                actual_result = self.click_menu_bt(str(n), elepath, name)
                if actual_result == 0:
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    actual_result = self.click_menu_bt(str(n), elepath, name)



            # time.sleep(3)
            # actual_result = self.click_menu_bt(n)
            #将进入应用界面的结果记录下来返回
            if actual_result == 0 or actual_result == 1:
                if n == 1:
                    actual_dict['wx'] = actual_result
                elif n == 2:
                    actual_dict['scene'] = actual_result
                elif n == 3:
                    actual_dict['DSPtf'] = actual_result
                elif n == 4:
                    actual_dict['SEMzs'] = actual_result
                elif n == 5:
                    actual_dict['tjzn'] = actual_result
                elif n == 6:
                    actual_dict['sjjcgj'] = actual_result
                elif n == 7:
                    actual_dict['znfx'] = actual_result
                elif n == 8:
                    actual_dict['sjkb'] = actual_result
                elif n == 9:
                    actual_dict['xsh'] = actual_result
                elif n == 10:
                    actual_dict['xxh'] = actual_result
                elif n == 11:
                    actual_dict['bdgl'] = actual_result
                elif n == 12:
                    actual_dict['wj'] = actual_result
                elif n == 13:
                    actual_dict['cj'] = actual_result
                elif n == 14:
                    actual_dict['tp'] = actual_result
                elif n == 15:
                    actual_dict['wtl'] = actual_result
                elif n == 16:
                    actual_dict['cpgl'] = actual_result
                elif n == 17:
                    actual_dict['khgl'] = actual_result
                elif n == 18:
                    actual_dict['wjgl'] = actual_result
                elif n == 19:
                    actual_dict['gysgl'] = actual_result
                elif n == 20:
                    actual_dict['yjgl'] = actual_result
                elif n == 21:
                    actual_dict['dxgl'] = actual_result
                elif n == 22:
                    actual_dict['wzgl'] = actual_result
                elif n == 23:
                    actual_dict['cygl'] = actual_result
                elif n == 24:
                    actual_dict['jsgl'] = actual_result
                elif n == 25:
                    actual_dict['mkgl'] = actual_result
                elif n == 26:
                    actual_dict['zdbgl'] = actual_result
                # continue
            n = n + 1

        return  actual_dict

    def click_menu(self,button_pos):
        if button_pos == '1':
            self.deprint("开始进入微信")
            button_id = 'module_1'

        if button_pos == '2':
            self.deprint("开始进入场景")
            button_id = 'module_5000'
        #
        # if button_pos == '3':
        #     self.deprint("开始进入DSP投放（ADTIME）")
        #     button_id = 'module_5001'
        #
        # if button_pos == '4':
        #     self.deprint("开始进入SEM助手（九枝兰）")
        #     button_id = 'module_5002'
        #
        # if button_pos == '5':
        #     self.deprint("开始进入图聚智能")
        #
        # if button_pos == '6':
        #     self.deprint("开始进入数据监测工具")
        #     button_id = 'module_5004'
        #
        if button_pos == '7':
            self.deprint("开始进入智能分析")
            button_id = 'module_5005'
        #
        if button_pos == '8':
            self.deprint("开始进入数据看板")
            button_id = 'module_5007'

        if button_pos == '9':
            self.deprint("开始进入线上会")
            button_id = 'module_2'

        if button_pos == '10':
            self.deprint("开始进入线下会")
            button_id = 'module_3'

        if button_pos == '11':
            self.deprint("开始进入表单管理")
            button_id = 'module_7'

        if button_pos == '12':
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
            self.deprint("开始进入内容管理")
            button_id = 'module_26'

        if button_pos == '23':
            self.deprint("开始进入成员管理")
            button_id = 'module_18'

        if button_pos == '24':
            self.deprint("开始进入角色管理")
            button_id = 'module_19'

        # if button_pos == '25':
        #     self.deprint("开始进入模块管理")

        if button_pos == '26':
            self.deprint("开始进入字典表管理")
            button_id = 'module_27'

        self.wait_is_visible('id', button_id)



if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    # o = ChoosePageTest(dr)
    # time.sleep(3)
    # actual_dict=o.cyclic_test_app(26)
    # o.click_menu_bt(25)
    # o.quit()