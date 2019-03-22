# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
import os
import subprocess
from  pages.management_tools.sms_pages import sms_create
from pages.management_tools.sms_pages.sms_create import SmsCreatePage
import datetime
import win32con
import win32gui
from selenium.webdriver.support.select import Select


class DetailSms(BasePage):

    # 导入收件人
    def export_receiver(self):
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到短信任务详情页面
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[2]/div[2]/button')  # 点导入收件人按钮
        time.sleep(1)
        print "点击上传文件按钮"
        self.wait_is_visible('x','//*[@id="importAddressee"]/div/div/div[2]/div/div[2]/div[2]/button')
        # 此处必须加点时间休息一下
        time.sleep(3)
        cur_path = os.path.abspath(os.path.dirname(__file__))
        con_path = "\common\\fileconfig\\file\phone.xlsx"
        sp_path = os.path.split(os.path.split(os.path.split(cur_path)[0])[0])[0]
        zh_path = eval(repr(sp_path + con_path).replace('\\', "\\"))
        # zh_path="D:\SmarketAutoTest\common\fileconfig\file\phone.xlsx"
        # print zh_path
        # # os.system(zh_path)
        # subprocess.call(zh_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # # os.system("D:\\upfile.exe")
        # self.deprint(u"try上传封面图成功")
        # win32gui
        dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, zh_path)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

        # # 获取上传文件路径
        # cur_path = os.path.abspath(os.path.dirname(__file__))
        # con_path = "\common\\fileconfig\\file\export_sms.exe"
        # print cur_path
        # # if type == 0:
        # #     con_path = "\common\\fileconfig\\file\export_sms.exe"
        # #     print con_path
        # # else:
        # #     con_path = "\common\\fileconfig\\file\timeexport.exe"
        # #     print con_path
        #
        # sp_path = os.path.split(os.path.split(os.path.split(cur_path)[0])[0])[0]
        # print sp_path
        # """
        # eval() 函数用来执行一个字符串表达式，并返回表达式的值,参考地址：http://www.runoob.com/python/python-func-eval.html
        # repr() 函数将对象转化为供解释器读取的形式，参考地址：http://www.runoob.com/python/python-func-repr.html
        # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次，
        #           参考地址：http://www.runoob.com/python/att-string-replace.html
        # """
        # zh_path = eval(repr(sp_path + con_path).replace('\\', '\\\\'))
        # self.deprint(u"上传的文件地址：" + zh_path)
        # # self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[2]/div[2]/button')  # 点上传文件按钮
        # """
        # python subprocess模块使用总结,参考地址：https://www.cnblogs.com/lincappu/p/8270709.html
        # """
        # subprocess.call(zh_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)##路径中有空格的采取此方法。没有空格的可以用os.system
        time.sleep(5)
        self.deprint("收件人上传成功")
        self.scrollbar("bottom")
        self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[3]/button')  # 点开始导入按钮导入文件
        time.sleep(5)
        self.deprint("开始导入收件人")
        time.sleep(2)
        # self.driver.refresh()
        # self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到短信任务详情页面

    # 点击启动发送，进行立即发送邮件
    def imme_send_sms(self):
        time.sleep(2)
        self.wait_is_visible('x','/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[8]/a')#点击“编辑短信内容”按钮
        self.element_value_input('x', '//*[@id="content"]',u'恭喜，您已成功报名参加人才交流大会，请凭获得的二维码参加会议。' )  # 输入短信内容
        self.wait_is_visible('x','//*[@id="editTask"]/div/div/div[3]/button[2]')#点击确定按钮
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[3]/button')  # 点击立即发送按钮
        self.wait_is_visible('x', '//*[@id="StartSend"]/div/div/div[3]/button[2]')  # 点击确定按钮

    #刷新页面查看回执
    def view_receipt_sms(self):
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        # self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        acount=self.find_element_text('x','/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[2]/div[1]/div[1]')
        self.deprint(u'收件人个数1'+acount)
        count=int(acount)
        s=0 #邮件返回回执数
        result=0
        for i in range(1,31):
            try:
                self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/span[3]')  # 进入发送任务管理
                iframe = self.driver.find_elements_by_tag_name("iframe")[0]
                self.driver.switch_to_frame(iframe)
                time.sleep(5)
                text=self.find_element_text('x','//*[@id="static-table"]/tbody/tr/td[6]/span[1]')
                result=""
                if text == u"成功":
                    result=u"成功"
                    break
                else:
                    self.deprint(u'查看回执')
                    time.sleep(10)
                    # self.driver.refresh()
                    self.wait_is_visible('x', '/html/body/div[1]/header/div/button/span')  # 点击右上角关闭按钮
                    self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档
                    # time.sleep(2)
            except:
                pass
            if i==30:
                result=u"短信发送超时"

        return result


    # 定时发送
    def timing_send_sms(self):
        time.sleep(2)
        # self.driver.refresh()
        # self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/span[3]')  # 进入发送任务管理
        # self.deprint("进入发送任务管理")
        # iframe = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[8]/iframe")
        # self.driver.switch_to_frame(iframe)
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[8]/a')  # 点击“编辑短信内容”按钮
        self.element_value_input('x', '//*[@id="content"]', u'恭喜，您已成功报名参加人才交流大会，请凭获得的二维码参加会议。')  # 输入短信内容
        self.wait_is_visible('x', '//*[@id="editTask"]/div/div/div[3]/button[2]')  # 点击确定按钮


        # """
        # timedelta参考地址：https://blog.csdn.net/alvin930403/article/details/54022338
        # """
        # time1 = (datetime.datetime.now() + datetime.timedelta(minutes=3)).strftime("%Y-%m-%d %H:%M") #在系统的时间基础上加一分钟

        # hour = time1[0:2]
        # min =  time1[3:2]
        # js = 'document.getElementById("sms_StartSend_sendTime").removeAttribute("readonly");'
        # self.driver.execute_script(js)

        time.sleep(2)
        hour = int((datetime.datetime.now() + datetime.timedelta()).strftime("%H"))-1
        min=int((datetime.datetime.now() + datetime.timedelta()).strftime("%M"))
        if min==59:
            time.sleep(60)
            self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[3]/div/a')  # 点击立即发送后面的小三角
            self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[3]/div/ul/li/a')  # 点击定时发送
            time.sleep(1)
            self.wait_is_visible('id', 'sms_StartSend_sendTime')
            hour = int((datetime.datetime.now() + datetime.timedelta()).strftime("%I")) - 1
            hele=self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/select[1]')
            Select(hele).select_by_index(hour)
            time.sleep(2)
            min = int((datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%M"))
            hmin=self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/select[2]')
            Select(hmin).select_by_index(min)
        else:
            self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[3]/div/a')  # 点击立即发送后面的小三角
            self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[3]/div/ul/li/a')  # 点击定时发送
            time.sleep(2)
            self.wait_is_visible('id','sms_StartSend_sendTime')
            # self.wait_is_visible('x', '//*[@id="sms_StartSend_sendTime"]')
            hour = int((datetime.datetime.now() + datetime.timedelta()).strftime("%I")) - 1
            hele = self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/select[1]')
            Select(hele).select_by_index(hour)
            time.sleep(2)
            min = int((datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%M"))
            hmin = self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/select[2]')
            Select(hmin).select_by_index(min)
        self.wait_is_visible('x','/html/body/div[6]/div[3]/div/button[1]')
        self.wait_is_visible('x','//*[@id="StartSend"]/div/div/div[3]/button[2]')
        # self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面




if __name__ == '__main__':
    time1 = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M")  # 在系统的时间基础上加一分钟
    print time1
    # dr = brower()
    # o = LoginPage(dr)
    # o.login()
    # o = ChoosePage(dr)
    # time.sleep(3)
    # o.click_menu_bt('21')
    # s = SmsCreatePage(dr)
    # s.list_sms()
    # p = DetailSms(dr)
    # # p.export_receiver()
    # # p.imme_send_sms()
    # p.view_receipt_sms()