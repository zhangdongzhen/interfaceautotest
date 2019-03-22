# -*- coding: utf-8 -*-
'''
Created on 2018-05-10
@author: 尤梅枝
'''
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
import os
import subprocess
from selenium.webdriver.common.action_chains import ActionChains
import datetime

from pages.off_line_meeting_pages.details_edm import Details_Edm

class Edm_Sms(BasePage):
    global count
    count=0

    def createEdm(self,type):
        time.sleep(8)
        self.deprint("开始执行邮件任务创建用例")
        self.wait_is_visible('x','/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/button') #点击新建任务
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[1]/div/input',u'自动化创建' + self.nowtime())#输入任务名称
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/input',u'自动化邮件标题')#输入邮件标题
        self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/button/span[2]')#点击任务分类
        if type=="邀请函":
            self.wait_is_visible('x', '//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[2]')
        if type=="感谢函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[3]')
        if type=="通知函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[4]')
        if type=="报名确认函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[5]')
        if type=="审核通过通知函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[6]')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="createTask"]/div/div/div[2]/form/div/div[5]/div/input').clear()#清空发件人显示名称
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[5]/div/input',u'自动化测试组')#填写发件人显示名称
        try:
            self.wait_is_visible('x', '//*[@id="createTask"]/div/div/div[3]/button[2]')  # 点击确定按钮
            return u'邮件创建成功'
        except:
            return u'邮件创建失败'

    def list_edm(self):#20180809
        time.sleep(15)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        self.wait_is_visible('x','/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a') #点击第一个邮件任务#20180809

    #编辑邮件#20180809
    def editEdm(self):
        self.deprint("开始执行邮件任务编辑用例")
        self.element_value_input('x','/html/body/div[3]/div[2]/div[2]/div[4]/input',u'自动化创建')
        self.wait_is_visible('x','/html/body/div[3]/div[2]/div[2]/button') #搜索自动化创建的邮件任务进行编辑
        for n in range(2,5):
            xpath='/html/body/div[3]/div[2]/div[3]/table/tbody/tr['+str(n)+']/td[10]'
            test=self.find_element_text('x',xpath)
            if test==u'正常':
                xpath2='/html/body/div[3]/div[2]/div[3]/table/tbody/tr['+str(n)+']/td[11]/a'
                self.wait_is_visible('x',xpath2)
                break
            else:
                continue
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        self.deprint("窗口切换成功")
        self.wait_is_visible('x','/html/body/div[3]/div[2]/div[3]/div[2]/div/div[1]/a[2]')
        time.sleep(1)
        iframe=self.driver.find_element_by_xpath('//*[@id="ueditor_0"]')
        self.driver.switch_to.frame(iframe) #切换iframe到邮件内容输入窗口
        self.deprint("iframe切换成功")
        self.wait_is_visible('x','/html/body')
        self.element_value_input('x','/html/body',u'自动化测试编辑的内容') #输入邮件内容
        self.driver.switch_to.default_content() #从邮件内容输入的iframe窗口切换回主文档
        self.deprint("从iframe切回主文档成功")
        self.scrollbar("bottom")
        self.wait_is_visible('x','/html/body/div[3]/div[2]/div[2]/form/div[6]/div/button') #点击保存按钮

    # 点击导入收件人#20180809
    def export(self,type):
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        # sc = self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[2]/button')  # 点导入收件人按钮
        # self.deprint(u"按钮1是：" + sc)
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[2]/button')  #点导入收件人按钮
        time.sleep(2)
        try :
            #获取上传文件路径
            cur_path = os.path.abspath(os.path.dirname(__file__))
            if type == 0 :
                con_path = "\common\\fileconfig\\file\export.exe"
            else :
                con_path = "\common\\fileconfig\\file\timeexport.exe"

            sp_path=os.path.split(os.path.split(os.path.split(cur_path)[0])[0])[0]
            # zh_path = sp_path + con_path
            zh_path = eval(repr(sp_path+con_path).replace('\\', '\\\\'))
            self.deprint(u"上传的文件地址："+zh_path )
            # name = self.find_element_text('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[2]/div[2]/button')  # 点上传文件按钮
            # self.deprint(u"按钮是：" + name)
            self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[2]/div[2]/button')  #点上传文件按钮
            time.sleep(1)
            # time.sleep(2)
            # p = os.system(zh_path)
            # p=subprocess.Popen(zh_path,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            subprocess.call(zh_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            time.sleep(8)
            fname = self.find_element_text('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[3]/div')  #上传成功后，“文件中包含数据条，每行数据包含个有效字段”显示验证上传成功
            self.deprint(u"上传的文件：" + fname)
        except:
            # 获取上传文件路径
            cur_path = os.path.abspath(os.path.dirname(__file__))
            if type == 0:
                con_path = "\common\\fileconfig\\file\export.exe"
            else:
                con_path = "\common\\fileconfig\\file\timeexport.exe"

            sp_path = os.path.split(os.path.split(os.path.split(cur_path)[0])[0])[0]
            # zh_path = sp_path + con_path
            zh_path = eval(repr(sp_path + con_path).replace('\\', '\\\\'))
            self.deprint(u"上传的文件地址：" + zh_path)
            # name = self.find_element_text('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[2]/div[2]/button')  # 点上传文件按钮
            # self.deprint(u"按钮是：" + name)
            self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[2]/div[2]/button')  # 点上传文件按钮
            time.sleep(1)
            # time.sleep(2)
            # p = os.system(zh_path)
            # p=subprocess.Popen(zh_path,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            subprocess.call(zh_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            time.sleep(8)
            fname = self.find_element_text('x',
                                           '//*[@id="importAddressee"]/div/div/div[2]/div/div[3]/div')  # 上传成功后，“文件中包含数据条，每行数据包含个有效字段”显示验证上传成功
            self.deprint(u"上传的文件：" + fname)

        self.deprint("收件人上传成功")
        self.scrollbar("bottom")
        self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[3]/button')  #点开始导入按钮导入文件
        time.sleep(8)
        self.deprint("开始导入收件人")
        self.driver.refresh()
        time.sleep(5)
        acount=self.find_element_text('x','/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[1]/div[1]/a')
        self.deprint(u'收件人个数1'+acount)



    # 点击编辑，进行编辑邮件内容#20180817
    def editMail(self):
        self.deprint("开始执行邮件任务编辑用例")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x','/html/body/div[1]/div[3]/div[1]/div[2]/div/div[7]/div[1]/div[2]/ul/li[3]/a')  # 点击编辑按钮
        self.deprint("点击编辑按钮成功")
        iframe = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[8]/iframe")
        self.driver.switch_to_frame(iframe)
        ifr = self.driver.find_element_by_xpath('//*[@id="ueditor_0"]')
        self.driver.switch_to.frame(ifr)  # 切换ifraself.driver.window_handles[-1]me到邮件内容输入窗口
        self.deprint("iframe切换成功")
        self.wait_is_visible('x', '/html/body')
        self.element_value_input('x', '/html/body', u'自动化编辑的内容')  # 输入邮件内容
        self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档
        self.deprint("从iframe切回主文档成功")
        self.scrollbar("bottom")
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/form/div[7]/div/input')  # 点击保存按钮

    # 点击启动发送，进行立即发送邮件#20180817
    def immeSendMail(self):
        time.sleep(2)
        # self.driver.refresh()
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/span[3]')  # 进入发送任务管理
        self.deprint("进入发送任务管理")
        # self.driver.refresh()
        # self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/span[3]')  # 进入发送任务管理
        # self.deprint("进入发送任务管理")
        iframe = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[8]/iframe")
        self.driver.switch_to_frame(iframe)
        self.wait_is_visible('x', '/html/body/div[1]/section/div/div[1]/div[2]/button[2]')  # 点击立即发送按钮
        self.wait_is_visible('x', '//*[@id="TaskSend"]/div/div/div[3]/button[2]')  # 点击确定按钮
        self.wait_is_visible('x', '/html/body/div[1]/header/div/button/span')  # 点击右上角关闭按钮
        self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档

    # 点击启动发送，进行立即发送邮件#20180817
    def immeSendMailNow(self):
        time.sleep(2)
        self.driver.refresh()
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[4]/div[2]/button')  # 点击启动发送按钮
        self.wait_is_visible('x', '//*[@id="TaskSend"]/div/div/div[3]/button[2]')  # 点击确定按钮


    #刷新页面查看回执#20180817
    def viewReceipt(self):
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        acount=self.find_element_text('x','/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[1]/div[1]/a')
        self.deprint(u'收件人个数1'+acount)
        count=int(acount)
        s=0 #邮件返回回执数
        # 15分钟内每间隔30秒刷新下清册
        for num in range(1,129):
            # self.driver.refresh()
            # time.sleep(3)
            # self.wait_is_visible('x', '/html/body/div[1]/header/div/button/span')  # 点击右上角关闭按钮
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/span[3]')  # 进入发送任务管理
            self.deprint("进入发送任务管理")
            iframe = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[8]/iframe")
            self.driver.switch_to_frame(iframe)
            time.sleep(8)
            for n in range(0,count):
                ele = '//*[@id="static-table"]/tbody/tr['+str(n+1)+']/td[6]'
                sendresult = self.find_element_text("x", ele)  # 获发送结果
                self.deprint(sendresult)
                # if sendresult<> '--' and sendresult.strip()<> '':
                if sendresult == '成功':
                    s=s+1

            if s ==count :
                result = 1
                self.deprint("邮件发送成功")
                break
            else:
                time.sleep(2)
                self.wait_is_visible('x', '/html/body/div[1]/header/div/button/span')  # 点击右上角关闭按钮
                self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档
                # time.sleep(2)


        if num == 450 :
            result = 0
            self.deprint(u'邮件发送超时')
        time.sleep(5)
        self.wait_is_visible('x', '/html/body/div[1]/header/div/button/span')  # 点击右上角关闭按钮
        self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档
        return result

    # 点击定时发送
    def timingSend(self):
        time.sleep(2)
        # self.driver.refresh()
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/span[3]')  # 进入发送任务管理
        self.deprint("进入发送任务管理")
        iframe = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[8]/iframe")
        self.driver.switch_to_frame(iframe)
        self.wait_is_visible('x', '/html/body/div[1]/section/div/div[1]/div[2]/div/a')  # 点击立即发送后面的小三角
        self.wait_is_visible('x', '/html/body/div[1]/section/div/div[1]/div[2]/div/ul/li/a')  # 点击定时发送
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        time1 = (datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")
        print time1
        # hour = time1[0:2]
        # min =  time1[3:2]
        self.driver.find_element_by_xpath('//*[@id="TaskSend"]/div/div/div[2]/div[4]/input').send_keys(time1)  # 修改时间为当前时间+1分钟
        self.wait_is_visible('x', '/html/body/div[5]/div[3]/div/button[1]')  # 点击确定按钮
        self.wait_is_visible('x', '//*[@id="TaskSend"]/div/div/div[3]/button[2]')  # 点击确定按钮
        self.wait_is_visible('x', '/html/body/div[1]/header/div/button/span')  # 点击右上角关闭按钮
        self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档




        self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档






if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('20')
    type="邀请函"
    S=Edm_Sms(dr)
    # S.createEdm(type)
    S.list_edm()
    # S.editMail()
    S.export()
    S.immeSendMail()
    S.viewReceipt()



    #e = Details_Edm(dr)
    #e.export_edm()

    # S.editEdm()
    # S.export()


