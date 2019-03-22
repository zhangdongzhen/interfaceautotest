# -*- coding: utf-8 -*-
'''
Created on 2018-07-16
@author: 尤梅枝
'''
from pages.common_pages.base import BasePage
from pages.wechat.create_material import Creat_media
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from selenium.webdriver.common.action_chains import ActionChains
from pages.common_pages.front_login import FrontLogin
import time
import random
class Create_vote(BasePage):
    #创建投票
    def new_vote(self,type,meetingtype):
        self.deprint("开始执行创建投票用例")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/button/span') #点击创建投票按钮
        title=u'自动化创建投票'+self.nowtime()
        self.element_value_input('id','pollTitle',title) #输入投票标题
        self.wait_is_visible('id','dropdownMenu3') #点击参与方式下拉框
        #type: 1 全部用户可参与  2 登陆后参与    3 关注微信后参与  4 报名会议后参与
        if type == 1 :
            self.wait_is_visible('x','//*[@aria-labelledby="dropdownMenu3"]/ul/li[1]') #选择全部用户可参与方式
            self.wait_is_visible('x', '//*[@class="tags"]/div[2]')
            self.wait_is_visible('x', '//*[@class="tags"]/div[3]/div/span[1]')  # 选择标签
        elif type == 2 :
            self.wait_is_visible('x','//*[@aria-labelledby="dropdownMenu3"]/ul/li[2]')  # 选择登录后参与
            self.wait_is_visible('id', 'dropdownMenu4')  # 点击注册表单下拉框
            time.sleep(2)
            self.wait_is_visible('x', '//*[@aria-labelledby="dropdownMenu4"]/ul/li[2]')  # 点击选择第2个注册表单
        elif type == 3 :
            self.wait_is_visible('x', '//*[@aria-labelledby="dropdownMenu3"]/ul/li[3]')  # 关注微信后参与
        else :
            self.wait_is_visible('x', '//*[@aria-labelledby="dropdownMenu3"]/ul/li[4]')  # 报名会议后参与

            meetingtype = '/html/body/div[1]/div[2]/main/div/div/div/div[2]/form/div[8]/div/div/div[4]/div/button'
            webinar = '/html/body/div[1]/div[2]/main/div/div/div/div[2]/form/div[8]/div/div/div[4]/div/div/ul/li[1]/a'
            offline = '/html/body/div[1]/div[2]/main/div/div/div/div[2]/form/div[8]/div/div/div[4]/div/div/ul/li[2]/a'
            meetingcombox = '//*[@id="dropdownMenu5"]'
            meeting = '/html/body/div[1]/div[2]/main/div/div/div/div[2]/form/div[8]/div/div/div[5]/div/div/div/input'
            webinarname = u'自动化创建会议2019-01-08 13:51:55'
            offlinename = u'自动化会议2018-11-18 20:46:50'
            confirmbutton = '/html/body/div[1]/div[2]/main/div/div/div/div[2]/form/div[8]/div/div/div[5]/div/div/div/div/button'
            meeting1 = '/html/body/div[1]/div[2]/main/div/div/div/div[2]/form/div[8]/div/div/div[5]/div/div/ul/li[1]/a[1]'
            if meetingtype == 1:
                self.choose_meeting(self, meetingtype, webinar, meetingcombox, meeting, webinarname, confirmbutton,
                                    meeting1)
            else:
                self.choose_meeting(self, meetingtype, offline, meetingcombox, meeting, offlinename, confirmbutton,meeting1)
        self.scrollbar('bottom')
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div/div/div[2]/div/button') #点击保存按钮
        time.sleep(2)
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button') #点击确定弹窗
        return title
    def setItems(self,sign):
        #找不到元素的问题还没有解决。。。
        # target = self.driver.find_element_by_xpath('//*[@id="left-menu"]/ul/li[2]/ul/li[1]')
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        # time.sleep(3)
        if sign == 1 :
            self.wait_is_visible('x', '//*[@id="left-menu"]/ul/li[1]/ul/li[1]/a')  # 点击姓名字段
            self.wait_is_visible('x', '//*[@id="left-menu"]/ul/li[1]/ul/li[2]/a')  # 点击手机
        self.wait_is_visible('x','//*[@id="left-menu"]/ul/li[1]/strong/span') #点击用户信息字段小三角收起
        self.wait_is_visible('x','//*[@id="left-menu"]/ul/li[2]/ul/li[1]/a') #选择单选题
        self.element_value_input('x', '//question-items/div[1]/div/text-field/div[1]/div[1]/div[1]/input', u'你的爱好？') #输入题目标题
        self.wait_is_visible('link',u'添加选项')
        self.element_value_input('x','//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[1]/div[1]/div/input',u'看电影') #输入题目选项
        self.wait_is_visible('link', u'添加选项')
        self.element_value_input('x', '//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[2]/div[1]/div/input', u'打乒乓') #输入题目选项
        self.wait_is_visible('link', u'添加选项')
        self.element_value_input('x','//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[3]/div[1]/div/input',u'睡觉觉') #输入题目选项
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/button') #点击保存按钮
        time.sleep(2)
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button') #点击确定弹窗
    def browse_vote(self):
        #sign : 1 投票内容有姓名手机3个单选题，2 姓名 ，3 3个单选题
        time.sleep(3)
        text=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div[2]/div[2]/span') #找到投票获取链接元素
        url1=text.get_attribute('innerText') #获取链接内容，链接内容后携带了【获取链接】部分文本
        url2=url1[0:28]      #截取文本，去掉【获取链接】
        js = 'window.open("' + url2 + '")'  #新开创建打开投票链接地址
        self.driver.execute_script(js)
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])  #切换到新开的窗口
        time.sleep(10)

    def fillin_vote(self,sign):
        #sign : 1：姓名手机3个单选题    2： 3个单选题   3：登陆后参与直接提交投票
        title = u'果果' + self.nowtime()
        if sign == 1 :
            self.element_value_input('x', '//*[@id="questionContainer"]/div[1]/div/div[1]/div/div/input', title)  # 输入投票姓名
            path ='//*[@id="questionContainer"]/div[1]/div/div[2]/div/div/input'#手机地址
            self.randome_phone(path)
            self.wait_is_visible('x', '//*[@id="questionContainer"]/div[1]/div/div[3]/ul/li[1]/label')  # 选择投票选项
        elif sign == 2:
            self.wait_is_visible('x','//*[@id="questionContainer"]/div[1]/div/div/ul/li[1]/label') #选择投票选项需要改
        else :
            self.deprint(u'登陆后参与')
        self.wait_is_visible('x', '//*[@id="questionContainer"]/div[2]/input')  # 提交投票需要改
        time.sleep(4)
        text2=self.find_element_text('x','/html/body/div/div/div/div[1]/p[1]') #获取投票提交结果页的提示信息作为判断是否成功的依据
        # print text2
        self.close()
        if sign == 1:
            return title
        else :
            return text2


    def randome_phone(self,path):

        list = ['131', '130', '132', '155', '156', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159',
                '182', '183', '184', '157', '187', '188', '147', '178', '185', '186', '145', '176', '185', '133', '153',
                '180', '181', '189', '177']
        for i in list:
            # 输入随机的手机号
            phone = self.randomphone()
            ranphone = i + str(phone)
            print "ranphone:", ranphone
            time.sleep(5)
            # 输入手机号
            ele = self.driver.find_element_by_xpath(path)
            ele.clear()
            self.find_element_input('x', path, ranphone)
            break
        return ranphone

    # 获取随机的手机后8位
    def randomphone(self):

        text = random.randint(00000000, 99999999)
        # textle = len(text)
        if text != 8:
            # text = text.zfill(8)   #自动前面补0  到8位
            text = '%08d' % text
        # print text
        return text



    def edit_vote(self):
        # self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[2]')
        element=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[2]')
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[1]/div[2]/a[3]/div/span')
        # self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button[2]')
        # self.scrollbar('bottom')
        # self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div/div/div[2]/div/button')
        # self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定弹窗
        # self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/button')  # 点击保存按钮
        # self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定弹窗

    #查看投票的数据统计
    def look_questionnaire_statistics(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到此问卷的数据统计页面
        self.driver.refresh()
        self.scrollbar('bottom')
        time.sleep(3)
        text1 = self.find_element_text('x', '/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]') # 获取收集概况-累计投票
        text2 = self.find_element_text('x','//*[@id="voterListScroller"]/table/tbody/tr[2]/td[1]')  # 获取最新数据记录-第一行投票ID不为空
        if text1 == '1' and text2.replace(' ','') <> '' :
            self.deprint(u'查看数据统计成功')
            return u"查看数据统计成功"
        else :
            return u"查看数据统计失败"

    #查看对应联系人互动及标签触发
    def look_contact_interaction(self,contactname,votename):
        self.deprint(u"开始查看对应联系人的互动及标签触发")
        self.deprint(str(contactname))
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到主界面
        object = ChoosePage(self.driver)
        object.click_menu_bt('17')
        # time.sleep(2)
        self.element_value_input('x', '/html/body/div[2]/div[2]/div[2]/div[1]/input', contactname) #在复合筛选中输入姓名的筛选条件进行筛选
        self.wait_is_visible('x', '/html/body/div[2]/div[2]/div[2]/div[1]/div/i')  # 点放大镜的筛选按钮
        # self.wait_is_visible('x', '/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[2]/a') #点标签快速筛选
        # self.wait_is_visible('x', '//*[@id="con-tagfilter"]/div[1]/div[1]/section[3]/div/label[2]')  # 点标签条件的第一个标签
        # self.wait_is_visible('x', '//*[@id="con-tagfilter"]/div[1]/div[2]/div/button')  # 点开始搜索
        time.sleep(1)
        table1 = self.driver.find_element_by_id("userContent")  #通过id获取整个表格对象
        trlist = table1.find_elements_by_tag_name("tr")
        # print u"对应联系人长度"+str(len(trlist))
        # 遍历所有数据获取姓名与参数一致的数据
        n = 1
        sign = 0
        for n in range(1, len(trlist)+1):
            ele = '//*[@id="userContent"]/tbody/tr[' + str(n) + ']/td[2]/div'
            result = self.find_element_text("x", ele)
            # self.deprint(result)
            if result == contactname:
                sign = n
                break
        if sign == 0 :
            self.deprint(u"没有找到对应的联系人")
        else :
            #找到对应联系人，查看联系人互动详情
            ele = '//*[@id="userContent"]/tbody/tr[' + str(sign) + ']/td[1]/div[2]/a' #点对应联系人的ID
            self.wait_is_visible('x', ele)
            time.sleep(1)
            iframe = self.driver.find_element_by_xpath("/html/body/div[2]/div[4]/iframe")
            self.driver.switch_to_frame(iframe)
            # time.sleep(2)
            self.wait_is_visible('x', '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/ul/li[2]/a')  # 点互动详情
            time.sleep(1)
            #获取第一行互动详情的对象标题
            text2 = self.find_element_text('x', '//*[@id="interaction-detail"]/div/table/tbody/tr[1]/td[6]/span[1]')
            #获取第一行互动详情的行为
            text3 = self.find_element_text('x', '//*[@id="interaction-detail"]/div/table/tbody/tr[1]/td[4]/span[1]')
            # # 获取第二行行互动详情的对象标题
            # text4 = self.find_element_text('x', '//*[@id="interaction-detail"]/div/table/tbody/tr[2]/td[6]/span[1]')
            # # 获取第二行互动详情的行为
            # text5 = self.find_element_text('x', '//*[@id="interaction-detail"]/div/table/tbody/tr[2]/td[4]/span[1]')
            self.deprint(str(votename))
            if text2 == votename and text3 == '提交投票' :
                self.deprint(u'对应联系人的互动详情成功')
                result1 = 1
            else :
                self.deprint(u'对应联系人的互动详情失败')
                result1 = 0

            #查看联系人标签详情
            # time.sleep(2)
            self.wait_is_visible('x', '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/ul/li[3]/a')  # 点标签详情
            time.sleep(1)
            table2 = self.driver.find_element_by_xpath('//*[@id="tag-detail"]/div/table/tbody')  # 通过xpath获取整个表格对象
            trlist2 = table2.find_elements_by_tag_name("tr")
            # 遍历所有数据获取行为对象与参数一致的数据
            m = 1
            result2= 0
            sign = 0
            for m in range(1, len(trlist2) + 1):
                #获取第一行标签详情的行为对象
                text6 = self.find_element_text('x', '//*[@id="tag-detail"]/div/table/tbody/tr[' + str(m) + ']/td[4]')
                if text6 == votename :
                    # 获取第一行标签详情的相关行为
                    sign = 1
                    text7 = self.find_element_text('x', '//*[@id="tag-detail"]/div/table/tbody/tr[' + str(m) + ']/td[3]')
                    if text7 == u'提交投票' :
                        self.deprint(u'对应联系人的标签详情成功')
                        result2 = 1
                        break
                    else :
                        self.deprint(u'对应联系人的标签详情失败')
                        result2 = 0
                        break
            if sign == 0:
                self.deprint(u'对应联系人的标签详情失败')
            if result1 == 1 and result2 == 1 :
                return u"查看对应联系人的互动和标签触发成功"
            else :
                return u"查看对应联系人的互动和标签触发失败"
    def addfields(self):
        self.wait_is_visible('x','//*[@id="left-menu"]/ul/li[1]/ul/li[1]')#添加姓名字段
        self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/button')  #点击保存按钮
        time.sleep(2)
        self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定弹窗

    def choose_meeting(self,typecombox,type,meetingcombox,meeting,meetingname,confirmbutton,meeting1):
        self.wait_is_visible('x',typecombox)  # 点会议类型下拉框
        self.wait_is_visible('x',type)  # 选择会议类型
        self.wait_is_visible('x', meetingcombox)  # 点击具体会议下拉框
        self.element_value_input('x',meeting,meetingname) #输入具体会议
        self.wait_is_visible('x',confirmbutton)  # 点击确定按钮
        self.wait_is_visible('x',meeting1)  # 点击选出的会议


if __name__ == '__main__':

    driver = brower()
    login= LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("1")
    test=Creat_media(driver)
    test.enter_vote()
    vote=Create_vote(driver)
    vote.new_vote()
    vote.setItems()
    vote.browse_vote()
