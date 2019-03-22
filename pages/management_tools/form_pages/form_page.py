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
import time
import random
# import requests
class Create_form(BasePage):
    #创建投票
    def new_form(self):
        time.sleep(8)
        self.deprint("开始执行创建表单用例")
        self.wait_is_visible('x','/html/body/div[2]/div[1]/main/div[1]/div[1]/div[2]/button') #点击新建表单按钮
        time.sleep(1)
        title=u'自动化创建表单'+self.nowtime()
        self.element_value_input('x','/html/body/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div/input',title) #输入表单标题
        self.wait_is_visible('id', 'dropdownMenu1')  # 点击类型下拉框
        self.wait_is_visible('x', '//*[@aria-labelledby="dropdownMenu1"]/ul/li[1]')  # 选择活动报名类型
        self.wait_is_visible('id','dropdownMenu2') #点击参与方式下拉框
        self.wait_is_visible('x','//*[@aria-labelledby="dropdownMenu2"]/ul/li[1]') #选择全部用户可参与方式
        self.wait_is_visible('x','//*[@class="tags"]/div[2]')
        self.wait_is_visible('x','//*[@class="tags"]/div[3]/div/span[1]') #选择标签
        self.scrollbar('bottom')
        self.wait_is_visible('x','/html/body/div[2]/div[1]/main/div/div[2]/div[1]/div[17]/div/button') #点击保存，进入编辑题目按钮
        time.sleep(4)
        self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定弹窗
        time.sleep(1)
        self.wait_is_visible('x', '//*[@id="j-maxheight"]/ul/li[1]/ul/li[1]/a')  # 点击姓名
        self.wait_is_visible('x', '//*[@id="j-maxheight"]/ul/li[1]/ul/li[2]/a')  # 点击手机
        self.wait_is_visible('x', '/html/body/div[2]/div[1]/main/div/div[2]/div/div[2]/div[1]/div[3]/div/button')  # 点击保存按钮
        time.sleep(1)
        self.wait_is_visible('x', '//*[@id="myModal"]/div/div/div[2]/button[1]')  # 点击弹出框确定按钮
        time.sleep(1)
        #进入推广链接界面
        div1 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div[1]/div[2]/div[1]/div[1]')
        ActionChains(self.driver).move_to_element(div1).perform()
        print "44"
        self.wait_is_visible('x', '/html/body/div[2]/div/main/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[2]/a[2]')  # 点击推广链接
        time.sleep(1)
        self.deprint("创建表单用例成功")
        return title




    def browse_form(self):
        # s = requests.Session()
        # s.cookies.clear()
        time.sleep(3)
        text=self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div/div[2]/div[2]/table/tbody/tr[1]/td[2]') #找到默认PC推广链接
        url1=text.get_attribute('innerText') #获取链接内容，链接内容后携带了【获取链接】部分文本
        url2=url1[0:34]      #截取文本，去掉【获取链接】
        js = 'window.open("' + url2 + '")'  #新开创建打开表单链接地址
        self.driver.execute_script(js)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])  #切换到新开的窗口
        time.sleep(3)
        title = u'乐乐' + self.nowtime()
        self.element_value_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[1]/div/input', title)  # 输入表单姓名
        phone = self.randome_phone()
        # self.element_value_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[2]/div/input', u'13278963454') #输入表单手机
        self.wait_is_visible('x','//*[@id="body-box"]/div[1]/div/div[2]/div[2]/input') #提交表单
        time.sleep(2)
        text2=self.find_element_text('x','/html/body/div/div/div/div[1]/p[1]') #获取表单提交结果页的提示信息作为判断是否成功的依据
        self.deprint(text2)
        return title,phone



    def edit_form(self):
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
        # self.driver.switch_to.window(self.driver.window_handles[1])  # 切换到此问卷的数据统计页面
        # self.wait_is_visible('x', '/html/body/div[2]/div[1]/header/div[2]/div[1]/ol/li[2]/a') #点表单列表
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到主页面
        object = ChoosePage(self.driver)
        object.click_menu_bt('11') #选择进入表单管理
        time.sleep(8)
        # self.driver.refresh()
        time.sleep(4)
        #进入表单的数据统计界面
        div1 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div[1]/div[2]/div[1]/div[1]')
        ActionChains(self.driver).move_to_element(div1).perform()
        # time.sleep(2)
        self.wait_is_visible('x', '//*[@class="item-cover"]/div/a[3]')  # 点击数据统计
        time.sleep(2)
        text1 = self.find_element_text('x', '/html/body/div[2]/div[1]/main/div[1]/div/div/div[1]/div[2]/div/p')  # 获取今日/累计收集
        text2 = self.find_element_text('x','//*[@id="shortTableScroll"]/table/tbody/tr/td[1]')  # 获取数据明细ID不为空
        if text1 == '1/1' and text2.replace(' ','') <> '' :
            self.deprint(u'查看数据统计成功')
            return u"查看数据统计成功"
        else :
            return u"查看数据统计失败"

    # #查看对应联系人互动及标签触发
    # def look_contact_interaction(self,formname):
    #     self.deprint(u"开始查看对应联系人的互动及标签触发")
    #     self.deprint(str(formname))
    #     self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到主界面
    #     object = ChoosePage(self.driver)
    #     object.click_menu_bt('17')
    #     # time.sleep(8)
    #     # modify_screen_resolution()
    #     self.wait_is_visible('x', '/html/body/div[2]/div[2]/div[2]/div[2]/div/button')  # 点查看其它用户
    #     self.wait_is_visible('x', '//*[@aria-labelledby="dropdownMenu1"]/li/a')  # 点匿名用户
    #     # time.sleep(1)
    #     self.wait_is_visible('x', '/html/body/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/div[2]/a')  # 点第一个匿名用户的ID
    #     time.sleep(5)
    #     iframe = self.driver.find_element_by_xpath("/html/body/div[2]/div[4]/iframe")
    #     self.driver.switch_to_frame(iframe)
    #     self.scrollbar("bottom")
    #     #找到第一个匿名联系人，查看联系人互动记录
    #     #获取第一行互动记录的互动对象
    #     showtext = self.find_element_text('x',
    #                                    '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[1]')
    #     if showtext == u'触发标签次数排行' :
    #         # 获取第一行互动记录的互动对象
    #         text2 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/table/tbody/tr[1]/td[3]')
    #         # time.sleep(1)
    #         #获取第一行互动记录的互动类型
    #         text3 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/table/tbody/tr[1]/td[1]')
    #         # time.sleep(1)
    #         #获取第一行互动记录的互动结果
    #         text4 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/table/tbody/tr[1]/td[4]/span')
    #         # time.sleep(1)
    #         if text2 == formname and text3 == '提交表单' and text4 == '成功' :
    #             self.deprint(u'对应联系人的互动详情成功')
    #             result1 = 1
    #         else :
    #             self.deprint(u'对应联系人的互动详情失败')
    #             result1 = 0
    #
    #         #查看联系人标签记录
    #         #获取第一行互动记录的对象
    #         text5 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[2]/table/tbody/tr[1]/td[3]')
    #         #获取第一行互动记录的行为
    #         text6 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[2]/table/tbody/tr[1]/td[2]')
    #         #获取第一行互动记录的触发标签
    #         text7 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[2]/table/tbody/tr[1]/td[4]')
    #         if text5 == formname and text6 == '提交表单' and text7 == '1' :
    #             self.deprint(u'对应联系人的标签触发成功')
    #             result2 = 1
    #         else :
    #             self.deprint(u'对应联系人的标签触发失败')
    #             result2 = 0
    #     else :
    #         # 获取第一行互动记录的互动对象
    #         text2 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[1]/div[2]/table/tbody/tr[1]/td[3]')
    #         # time.sleep(1)
    #         #获取第一行互动记录的互动类型
    #         text3 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[1]/div[2]/table/tbody/tr[1]/td[1]')
    #         # time.sleep(1)
    #         #获取第一行互动记录的互动结果
    #         text4 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[1]/div[2]/table/tbody/tr[1]/td[4]/span')
    #         # time.sleep(1)
    #         if text2 == formname and (text3 == '提交表单' or text3 == '浏览表单' )and text4 == '成功' :
    #             self.deprint(u'对应联系人的互动详情成功')
    #             result1 = 1
    #         else :
    #             self.deprint(u'对应联系人的互动详情失败')
    #             result1 = 0
    #
    #         #查看联系人标签记录
    #         #获取第一行互动记录的对象
    #         text5 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[7]/div[2]/table/tbody/tr[1]/td[3]')
    #         #获取第一行互动记录的行为
    #         text6 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[7]/div[2]/table/tbody/tr[1]/td[2]')
    #         #获取第一行互动记录的触发标签
    #         text7 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[7]/div[2]/table/tbody/tr[1]/td[4]')
    #         if text5 == formname and (text6 == '提交表单' or text6 == '浏览表单') and text7 == '1' :
    #             self.deprint(u'对应联系人的标签触发成功')
    #             result2 = 1
    #         else :
    #             self.deprint(u'对应联系人的标签触发失败')
    #             result2 = 0
    #     print str(text3)
    #     print str(text6)
    #     if result1 == 1 and result2 == 1:
    #         return u"查看对应联系人的互动和标签触发成功"
    #     else:
    #         return u"查看对应联系人的互动和标签触发失败"


    #查看对应联系人互动及标签触发
    def look_contact_interaction(self,contactname,formname,phone):
        self.deprint(u"开始查看对应联系人的互动及标签触发")
        self.deprint(str(contactname))
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到主界面
        object = ChoosePage(self.driver)
        object.click_menu_bt('17')
        # time.sleep(2)
        self.element_value_input('x', '/html/body/div[2]/div[2]/div[2]/div[1]/input', phone) #在复合筛选中输入姓名的筛选条件进行筛选
        self.wait_is_visible('x', '/html/body/div[2]/div[2]/div[2]/div[1]/div/i')  # 点放大镜的筛选按钮
        # self.wait_is_visible('x', '/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[2]/a') #点标签快速筛选
        # self.wait_is_visible('x', '//*[@id="con-tagfilter"]/div[1]/div[1]/section[3]/div/label[2]')  # 点标签条件的第一个标签
        # self.wait_is_visible('x', '//*[@id="con-tagfilter"]/div[1]/div[2]/div/button')  # 点开始搜索
        time.sleep(8)
        table1 = self.driver.find_element_by_xpath('//*[@id="userContent"]/tbody')  #通过id获取整个表格对象
        trlist = table1.find_elements_by_tag_name("tr")
        print u"对应联系人个数"+str(len(trlist))
        # 遍历所有数据获取姓名与参数一致的数据
        n = 1
        sign = 0
        for n in range(1, len(trlist)+1):
            ele = '//*[@id="userContent"]/tbody/tr[' + str(n) + ']/td[2]/div'
            result = self.find_element_text("x", ele)
            # self.deprint(result)
            if result == contactname:
                sign = n
                self.deprint(u'找到提交表单联系人成功')
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
            self.deprint(u'进入联系人互动详情页面')
            time.sleep(3)
            path = '//*[@id="interaction-detail"]/div/table/tbody'
            result1 = self.look_interaction(path,'1')


            #查看联系人标签详情
            # time.sleep(2)
            self.wait_is_visible('x', '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/ul/li[3]/a')  # 点标签详情
            time.sleep(3)
            path1 = '//*[@id="tag-detail"]/div/table/tbody'
            result2 = self.look_interaction(path1,'2')
            if result1 == '1' and result2 == '1' :
                return u"查看对应联系人的互动和标签触发成功"
            else :
                return u"查看对应联系人的互动和标签触发失败"

    # 生成随机手机号码函数

    def randome_phone(self):
        ranphone=''
        list = ['131', '130', '132', '155', '156', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159',
                '182', '183', '184', '157', '187', '188', '147', '178', '185', '186', '145', '176', '185', '133', '153',
                '180', '181', '189', '177']
        for i in list:
            # 输入随机的手机号
            phone = self.randomphone()
            ranphone = i + str(phone)
            print "ranphone:", ranphone
            time.sleep(5)
            # 输入随机的手机号码s
            self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[2]/div/input', ranphone)
            break

        return  ranphone

    # 获取随机的手机后8位
    def randomphone(self):

        text = random.randint(00000000, 99999999)
        # textle = len(text)
        if text != 8:
            # text = text.zfill(8)   #自动前面补0  到8位
            text = '%08d' % text
        # print text
        return text

    def look_interaction(self,xpath3,flag):
        # 获取所有的互动类型，进行匹配
        # 获取了互动记录表格元素
        tableelement = self.driver.find_element_by_xpath(xpath3)
        trelements = tableelement.find_elements_by_tag_name("tr")
        # arrrylist将保存所有互动类型的值

        arrrylist = []
        if flag == "1":
            self.deprint(u'开始获取联系人的所有互动类型')
            for i in trelements:
                tdlist = i.find_elements_by_tag_name("td")
                time.sleep(1)
                print tdlist[3].text
                arrrylist.append(tdlist[3].text)

        else:
            self.deprint(u'开始获取联系人的所有标签触发类型')
            for i in trelements:
                tdlist = i.find_elements_by_tag_name("td")
                time.sleep(1)
                print tdlist[2].text
                arrrylist.append(tdlist[2].text)

        # 此时进行匹配
        # if "浏览表单" in arrrylist:
        #     arrrylist.remove("浏览表单")
        #     text1 = "1"
        # else:
        #     text1 = "0"

        if "提交表单" in arrrylist:
            arrrylist.remove("提交表单")
            text = "1"
        else:
            text = "0"

        # if text == "1" and text1 == "1":
        if text == "1" :
            self.deprint(u'查找提交表单互动或标签触发成功')
            result = '1'
        else:
            self.deprint(u'查找提交表单互动或标签触发失败')
            result = '0'
        return result

    #配置表单
    def config_customform(self,education,industry,gradutime,edupic):
        #点配置表单
        self.wait_is_visible('x', '//*[@id="g-right"]/div/div[1]/div[2]/table/tbody/tr/td[9]/a[5]')
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #点保存按钮
        self.wait_is_visible('x', '/html/body/div[2]/div/main/div/div[2]/div[1]/div[17]/div/button')
        time.sleep(1)
        #点弹框的确定按钮
        self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')
        time.sleep(4)
        #鼠标滑到表单上点字段设置
        div1 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div[1]/div[2]/div[1]/div[1]')
        ActionChains(self.driver).move_to_element(div1).perform()
        self.wait_is_visible('x', '/html/body/div[2]/div/main/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a[2]')  # 点击字段设置
        time.sleep(5)
        scrollele = self.driver.find_element_by_class_name('ps-scrollbar-y')
        # js = "var q=document.getElementsByClassName(\"ps-scrollbar-y\")[0];q.style.top = \"300\";"
        # self.driver.execute_script(js)

        #查看是否有新增的字段
        target = self.driver.find_element_by_xpath('//*[@id="j-maxheight"]/ul/li/ul/li[14]/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        education1 = self.find_element_text('x', '//*[@id="j-maxheight"]/ul/li/ul/li[14]/a')
        industry1 = self.find_element_text('x', '//*[@id="j-maxheight"]/ul/li/ul/li[15]/a')
        gradutime1 = self.find_element_text('x', '//*[@id="j-maxheight"]/ul/li/ul/li[16]/a')
        edupic1 = self.find_element_text('x', '//*[@id="j-maxheight"]/ul/li/ul/li[17]/a')
        if education1 == education and industry1 == industry and gradutime1 == gradutime and edupic1 == edupic :
            result = 1
            self.wait_is_visible('x',
                                 '//*[@id="j-maxheight"]/ul/li/ul/li[14]/a')
            self.wait_is_visible('x',
                                 '//*[@id="j-maxheight"]/ul/li/ul/li[15]/a')
            self.wait_is_visible('x',
                                 '//*[@id="j-maxheight"]/ul/li/ul/li[16]/a')
            self.wait_is_visible('x',
                                 '//*[@id="j-maxheight"]/ul/li/ul/li[17]/a')
            self.scrollbar('bottom')
            #将新增的字段设置必填
            self.wait_is_visible('x', '/html/body/div[2]/div/main/div/div[2]/div/div[2]/div[1]/div[14]/div/div[1]/div[4]/label/div/input')
            self.wait_is_visible('x', '/html/body/div[2]/div/main/div/div[2]/div/div[2]/div[1]/div[15]/div/div[1]/div[4]/label/div/input')
            self.wait_is_visible('x', '/html/body/div[2]/div/main/div/div[2]/div/div[2]/div[1]/div[16]/div/div[1]/div[5]/label/div/input')
            self.wait_is_visible('x', '/html/body/div[2]/div/main/div/div[2]/div/div[2]/div[1]/div[17]/div/div[1]/div[4]/label/div/input')

            #实现拖动元素，调整报道时间和学历文件的位置

            # source = self.driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div/div[2]/div[1]/div[16]')
            # target = self.driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div/div[2]/div[1]/div[17]')
            # time.sleep(1)
            # actions = ActionChains(self.driver)
            # actions.drag_and_drop(source, target)
            # actions.perform()

            time.sleep(2)
            #点保存按钮
            self.wait_is_visible('x', '/html/body/div[2]/div/main/div/div[2]/div/div[2]/div[1]/div[18]/div/button')
            time.sleep(3)
            #点提示确认按钮
            self.wait_is_visible('x', '//*[@id="myModal"]/div/div/div[2]/button[1]')
            time.sleep(1)

        else :
            result = 0

        return result

    #报名表单左侧可选字段中不显示上述被去掉的字段
    def lookformfields(self,education,industry,registtime,edupic):
        time.sleep(5)
        #点配置表单
        self.wait_is_visible('x', '//*[@id="g-right"]/div/div[1]/div[2]/table/tbody/tr/td[9]/a[5]')
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #点保存按钮
        self.wait_is_visible('x', '/html/body/div[2]/div/main/div/div[2]/div[1]/div[17]/div/button')
        time.sleep(1)
        #点弹框的确定按钮
        self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')
        time.sleep(4)
        #鼠标滑到表单上点字段设置
        div1 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div[1]/div[2]/div[1]/div[1]')
        ActionChains(self.driver).move_to_element(div1).perform()
        self.wait_is_visible('x', '/html/body/div[2]/div/main/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a[2]')  # 点击字段设置
        time.sleep(5)
        #点弹框的确认按钮
        self.wait_is_visible('x', '//*[@id="myModal"]/div/div/div[2]/button[1]')
        time.sleep(1)

        sign = 1
        #遍历左侧的字段，查看是否有新增的字段
        ulele = self.driver.find_element_by_xpath('//*[@id="j-maxheight"]/ul/li/ul')
        lilist = ulele.find_elements_by_tag_name('li')
        for n in range(len(lilist), 0, -1):
            ele = self.find_element_text('x', '//*[@id="j-maxheight"]/ul/li/ul/li['+str(n)+']')
            if ele == education or ele == industry or ele == registtime or ele == edupic:
                sign = 0
                break

        return sign




if __name__ == '__main__':


    driver = brower()
    login= LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("11")
    form=Create_form(driver)
    form.new_form()
    form.browse_form()