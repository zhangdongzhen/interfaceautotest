# -*- coding: utf-8 -*-
'''
Created on 2018-07-16
@author: 张站平
'''
from pages.common_pages.base import BasePage
from pages.wechat.create_material import Creat_media
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from selenium.webdriver.common.action_chains import ActionChains
import time
class Create_microdiscussion(BasePage):
    #创建微讨论
    def new_microdiscussion(self,forumtype):
        #1:微论坛 (1、创建允许匿名发主帖的微论坛--2、创建子板)
        #2:留言板
        #3:评论区
        time.sleep(8)
        if forumtype == 1 :
            self.deprint("开始执行创建微讨论用例")
            self.wait_is_visible('x','/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/button') #点击新建论坛按钮
            title=u'自动化微论坛'+self.nowtime()
            self.deprint('' + title)
            self.element_value_input('x','//*[@id="createforum"]/div/div/div[2]/div[2]/div/div/input',title) #输入论坛名称
            self.wait_is_visible('x', '//*[@id="createforum"]/div/div/div[3]/button[2]')  # 点击保存按钮
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a')  # 点击微论坛名称
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[4]/div/span/a')  # 点设置子版
            time.sleep(1)
            iframe = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/iframe')
            self.driver.switch_to_frame(iframe)
            self.wait_is_visible('x','//*[@id="con-local"]/div[1]/div[2]/button') #点新建子版
            self.element_value_input('x', '//*[@id="versionName"]', u'自动化子版')  # 输入子版名称
            self.wait_is_visible('x','//*[@id="addVersion"]/tr/td[3]/div/button[1]') #点子版名称后面的对勾
            self.driver.switch_to.parent_frame()# 从iframe窗口切换回主文档
            # self.close()
            # time.sleep(1)
            # self.driver.switch_to.window(self.driver.window_handles[0])
            self.deprint("创建微论坛和设置子版用例成功")
            self.driver.refresh()
            return title
        elif forumtype == 2 :
            self.deprint("开始执行创建留言板用例")
            self.wait_is_visible('x','/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/button') #点击新建论坛按钮
            self.wait_is_visible('x', '//*[@id="createforum"]/div/div/div[2]/div[1]/div/div[1]/button')  # 点击论坛类型下拉框
            self.wait_is_visible('x', '//*[@id="createforum"]/div/div/div[2]/div[1]/div/div[1]/ul/li[2]')  # 选择留言板
            title=u'自动化留言板'+self.nowtime()
            self.deprint(''+title)
            self.element_value_input('x','//*[@id="createforum"]/div/div/div[2]/div[2]/div/div/input',title) #输入论坛名称
            self.wait_is_visible('x', '//*[@id="createforum"]/div/div/div[3]/button[2]')  # 点击保存按钮
            self.deprint("创建留言板用例成功")
            return title
        else :
            self.deprint("开始执行创建评论区用例")
            self.wait_is_visible('x','/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/button') #点击新建论坛按钮
            self.wait_is_visible('x', '//*[@id="createforum"]/div/div/div[2]/div[1]/div/div[1]/button')  # 点击论坛类型下拉框
            self.wait_is_visible('x', '//*[@id="createforum"]/div/div/div[2]/div[1]/div/div[1]/ul/li[3]')  # 选择评论区
            title=u'自动化评论区'+self.nowtime()
            self.deprint(''+title)
            self.element_value_input('x','//*[@id="createforum"]/div/div/div[2]/div[2]/div/div/input',title) #输入论坛名称
            self.wait_is_visible('x', '//*[@id="createforum"]/div/div/div[3]/button[2]')  # 点击保存按钮
            time.sleep(4)
            self.deprint("创建评论区用例成功")
            self.close()
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[0])
            return title



    def publish_post(self):
        #PC（WAP）端发表帖子--
        #增加互动：发帖
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a')  # 点击第一个微讨论的名称链接进去
        time.sleep(1)
        self.wait_is_visible('x','/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点击pc预览
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x','/html/body/div[2]/div/div[3]/div[2]/button')  # 选择我要发帖
        time.sleep(1)
        title = u'自动化帖子' + self.nowtime()
        self.element_value_input('x', '//*[@id="leaveMsg"]/div/div/div[2]/div[1]/div[1]/div/input', title)  # 输入标题
        iframe = self.driver.find_element_by_xpath('//*[@id="ueditor_0"]')
        self.driver.switch_to_frame(iframe)
        self.wait_is_visible('x', '/html/body')
        self.element_value_input('x', '/html/body', u'自动化')  # 输入帖子内容
        self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档
        self.wait_is_visible('x', '//*[@id="_addPostButon_id"]')  # 点击发布
        time.sleep(1)
        self.close()
        self.deprint(u"微论坛发帖成功")
        return title

    def add_interaction(self,title):
        #3、后台查看，设为置顶和热帖 - -4、PC（wap)端点赞 - -5、后台查看 - -6、帖子点赞量统计正确 - -7、PC(wap)
        #端删除帖子 - -8、后台查看，不再显示被删除的帖子
        self.deprint(title)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        #后台帖子置顶
        self.scrollbar('bottom')
        table1 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody")  #通过xpath获取整个表格对象
        trlist = table1.find_elements_by_tag_name("tr")
        # print len(trlist)
        # 遍历所有数据找到新增的帖子
        n = 1
        sign = 0
        for n in range(1, len(trlist)+1):
            ele = '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[3]/a'
            result = self.find_element_text("x", ele)
            self.deprint(result)
            if result == title:
                sign = n
                break
        if sign == 0 :
            self.deprint(u"没有找到对应的帖子")
        else :
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[8]/div/div/a')  # 点击新帖后面的三个小黑点
            self.wait_is_visible('x','/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[8]/div/div/ul/li[1]/a') #点置顶
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[8]/div/div/a')  # 点击新帖后面的三个小黑点
            self.wait_is_visible('x','/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[8]/div/div/ul/li[2]/a') #点加精
            self.scrollbar('top')
            self.wait_is_visible('x','/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            #获取第一个帖子是否有置顶和精字眼，打印置顶成功
            text1 = self.find_element_text("x", '/html/body/div[2]/div/div[3]/div[4]/div/div[2]/div[1]/div/span[1]') #置顶字眼
            text2 = self.find_element_text("x", '/html/body/div[2]/div/div[3]/div[4]/div/div[2]/div[1]/div/span[2]') #精字眼
            # print str(text2)
            if text1 == u'置顶' :
                r1 = 1
                self.deprint(u'置顶成功')
            else:
                r1 = 0
                self.deprint(u'置顶失败')

            if text2 == u'精' :
                r2 = 1
                self.deprint(u'加精成功')
            else :
                r2 = 0
                self.deprint(u'加精失败')

            self.wait_is_visible('x', '/html/body/div[2]/div/div[3]/div[4]/div/div[2]/div[3]/div[2]/a[4]')  # 点赞
            self.close()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.refresh()
            time.sleep(2)
            text2 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[2]/div[3]/div[5]/div/span') #主帖列表的点赞数
            text3 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[6]') #清册里的点赞数
            if text2 == '1' and text3 == '1' :
                r3 = 1
                self.deprint(u"点赞成功")
            else :
                r3 = 1
                self.deprint(u"点赞失败")


        #pc端删除帖子
        self.wait_is_visible('x', '/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
        time.sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[2]/div/div[3]/div[4]/div/div[2]/div[3]/div[2]/a[2]/span')  # 点第一个帖子的小桶
        # time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[4]/div/div/div[3]/button[2]')  # 点删除讨论版的确定按钮
        time.sleep(4)
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        time.sleep(4)
        text4 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div/span')  #获取总贴数

        if text4 == '0' :
            r4 = 1
            self.deprint(u"后台查看删帖成功")
        else :
            r4 = 0
            self.deprint(u"后台查看删帖失败")
        # self.scrollbar('200')
        # table1 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody")  #通过xpath获取整个表格对象
        # trlist = table1.find_elements_by_tag_name("tr")
        # if len(trlist) == 0 :
        #     r4 = 1
        #     self.deprint(u"删帖成功")
        # else :
        #     r4 = 0
        #     self.deprint(u"删帖失败")
        # self.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return r1, r2, r3, r4


    def modify_limitlogin(self,limittype):
        #开始 微论坛、留言板 -9、修改为仅登；录后发帖--10、未登录状态下进入PC(WAP)端发帖，跳转到登录页面-
        # if limittype == 1 :
        #     self.driver.switch_to.window(self.driver.window_handles[-1])
        #     self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a') #点微论坛名称链接
        # time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div/div[2]/div[4]/a[1]/i')  # 点编辑按钮
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/button')  # 点主帖限制
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/ul/li[4]')  # 选择仅登录可以发主帖
        time.sleep(1)
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[2]/button')  # 点请选择注册表单
        # self.wait_is_visible('x','//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[2]/ul/li[2]')  # 选择新建注册表单(9)
        self.nameofform(u"新建注册表单(9)")
        self.wait_is_visible('x','//*[@id="editforum"]/div/div/div[3]/button')  # 点保存按钮
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #limittype :1 微论坛， 2留言板
        if limittype == 1 :
            self.wait_is_visible('x', '/html/body/div[2]/div/div[3]/div[2]/button')  # 点我要发帖
        else :
            self.wait_is_visible('x', '/html/body/div[1]/div/div[3]/div[2]/button')  # 点我要留言
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        text1 = self.find_element_text("x", '//*[@id="one1"]') #未登录发帖跳到登陆界面，获取到登陆页面的显示文字“普通登录”
        # print str(text1)
        if text1.replace(' ','') == u'普通登录' :
            if limittype == 1 :
                self.deprint(u'仅登录可以发主帖成功')
                result1 = 1
            else :
                self.element_value_input('x', '//*[@id="con_one_1"]/div[1]/input','18732159800')  # 输入用户名
                self.element_value_input('x', '//*[@id="con_one_1"]/div[3]/input', '123123')  # 输入密码
                self.wait_is_visible('x', '//*[@id="con_one_1"]/input')  # 点登陆按钮
                time.sleep(5)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.wait_is_visible('x', '/html/body/div[1]/div/div[3]/div[2]/button')  # 点我要留言
                time.sleep(3)
                text4 = self.find_element_text("x", '//*[@id="_addPostButon_id"]')  # 获取到发布留言的发布按钮即可
                if text4.replace(' ','') == u'发布' :
                    self.deprint(u'仅登录可以发主帖成功')
                    result1 = 1
                else :
                    self.deprint(u'仅登录可以发主帖失败')
                    result1 = 0

        else :
            self.deprint(u'仅登录可以发主帖失败')
            result1 = 0
        self.close()
        return result1
        # 结束


    def modify_microdiscussion_limitclose(self):
        #开始 微论坛 11、修改为关闭前台发帖--12、PC（WAP）端查看，无发帖按钮
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # time.sleep(2)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[4]/a[1]')  # 点编辑按钮
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/button')  # 点主帖限制
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/ul/li[5]')  # 选择关闭前台发布主帖
        self.wait_is_visible('x','//*[@id="editforum"]/div/div/div[3]/button')  # 点保存按钮
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # time.sleep(8)
        self.scrollbar('400')
        text2 = self.find_element_text("x", '/html/body/div[2]/div/div[3]/div[3]/div[2]')  # 关闭前台发帖无发帖按钮，获取页面的提示信息“该论坛已关闭”
        if text2 == u'该论坛已关闭' :
            self.deprint(u'微论坛关闭前台发布主帖成功')
            result2 = 1
        else :
            self.deprint(u'微论坛关闭前台发布主帖失败')
            result2 = 0
        # operlist = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]')
        # divList = operlist.find_elements_by_tag_name("div")
        # print len(divList)
        # if len(divList) == 3:
        #     self.deprint(u'微论坛关闭前台发布主帖成功')
        #     result2 = 1
        # else:
        #     self.deprint(u'微论坛关闭前台发布主帖失败')
        #     result2 = 0
        self.close()
        return result2
        #结束


    def modify_microdiscussion_adminpost(self):
        #开始 微论坛 13、管理员发帖--14、PC(WAP)端查看,不能编辑和删除
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # time.sleep(2)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[4]/a[1]')  # 点编辑按钮
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/button')  # 点主帖限制
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/ul/li[1]')  # 选择允许匿名发主帖
        self.wait_is_visible('x','//*[@id="editforum"]/div/div/div[3]/button')  # 点保存按钮
        time.sleep(1)
        self.scrollbar('200')
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/button')  # 点发帖按钮
        time.sleep(1)
        iframe = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/iframe')
        self.driver.switch_to_frame(iframe)
        title1 = u'自动化管理员发帖' + self.nowtime()
        self.element_value_input('x', '//*[@id="AddMicroForumPostWindow"]/div[3]/div[3]/div[1]/div[2]/div/input', title1)  # 输入主帖标题
        self.wait_is_visible('x', '//*[@id="AddMicroForumPostWindow"]/div[3]/div[3]/div[3]/div[2]/div/button/span[1]')  # 点击所属子版
        self.wait_is_visible('x','//*[@id="AddMicroForumPostWindow"]/div[3]/div[3]/div[3]/div[2]/div/ul/li[2]')  # 选择第一个子版
        self.wait_is_visible('x','//*[@id="AddMicroForumPostWindow"]/div[3]/div[3]/div[5]/div[2]/div[2]/label[1]')  # 选择发帖身份-管理员
        iframe = self.driver.find_element_by_xpath('//*[@id="ueditor_0"]')
        self.driver.switch_to_frame(iframe)
        self.element_value_input('x', '/html/body',u'管理员发帖内容')  # 输入主帖标题
        self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档
        self.scrollbar('bottom')
        self.wait_is_visible('x', '//*[@id="AddMicroForumPostWindow"]/div[3]/div[3]/div[7]/button') #点保存按钮
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
        time.sleep(2)
        #获取每个帖子的操作按钮数目（管理员 2个，  匿名用户  4个）
        self.driver.switch_to.window(self.driver.window_handles[-1])
        operlist = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[4]/div/div[2]/div[3]/div[2]')
        aList = operlist.find_elements_by_tag_name("a")
        # print len(aList)
        if len(aList) == 2 :
            self.deprint(u'微论坛管理员发帖成功')
            result3 = 1
        else :
            self.deprint(u'微论坛管理员发帖失败')
            result3 = 0

        return result3


        #结束

    def publish_message(self):
        #PC（WAP）端发表留言--
        #增加互动：发留言
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a')  # 点击第一个留言板的名称链接进去
        time.sleep(1)
        self.wait_is_visible('x','/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点击pc预览
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x','/html/body/div[1]/div/div[3]/div[2]/button')  # 选择我要留言
        time.sleep(1)
        title = u'自动化留言' + self.nowtime()
        self.element_value_input('x', '//*[@id="leaveMsg"]/div/div/div[2]/div/div/div[1]/div', title)  # 输入留言内容
        self.wait_is_visible('x', '//*[@id="_addPostButon_id"]')  # 点击发布
        time.sleep(1)
        self.close()
        self.deprint(u"发布留言成功")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        #后台遍历查看清册数据行数和数据的主帖内容是否与增加的一致
        self.scrollbar('bottom')
        table1 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody")  #通过xpath获取整个数据行
        trlist = table1.find_elements_by_tag_name("tr")
        if len(trlist) > 0 :
            text2 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[3]/a') #获取第一个数据行的主帖内容
            if text2 == title :
                self.deprint(u"后台查看发布的留言成功")
                result = 1
        return title

    def add_message_interaction(self,title):
        #、PC(wap)端点赞--5、后台查看,帖子点赞量统计正确--6、PC（WAP)端删除留言--7、后台查看，不再显示被删除的帖子
        self.scrollbar('top')
        self.wait_is_visible('x','/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/a[2]')  # 点赞按钮
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        time.sleep(2)
        text2 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[2]/div[3]/div[5]/div/span') #主帖列表的点赞数
        self.scrollbar('200')
        text3 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[5]') #清册里的点赞数
        if text2 == '1' and text3 == '1' :
            r1 = 1
            self.deprint(u"后台查看留言点赞量统计正确")
        else :
            r1 = 0
            self.deprint(u"后台查看留言点赞量统计失败")

        #pc端删除帖子
        self.scrollbar('top')
        self.wait_is_visible('x', '/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div[2]/div[2]/a[2]/span')  # 点第一个帖子的小桶
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[3]/div/div/div[3]/button[2]')  # 点删除讨论版的确定按钮
        time.sleep(4)
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        time.sleep(3)
        text4 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div/span')  #获取总贴数

        if text4 == '0' :
            r2 = 1
            self.deprint(u"后台查看删帖成功")
        else :
            r2 = 0
            self.deprint(u"后台查看删帖失败")
        # self.scrollbar('200')
        # table1 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody")  #通过xpath获取整个表格对象
        # trlist = table1.find_elements_by_tag_name("tr")
        # if len(trlist) == 0 :
        #     r2 = 1
        #     self.deprint(u"后台查看留言删帖成功")
        # else :
        #     r2 = 0
        #     self.deprint(u"后台查看留言删帖失败")
        return r1,r2

    def modify_message_limitclose(self):
        # 开始 留言板 11、修改为关闭前台发帖--12、PC（WAP）端查看，无发帖按钮
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # time.sleep(2)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[4]/a[1]')  # 点编辑按钮
        self.wait_is_visible('x',
                             '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/button')  # 点主帖限制
        self.wait_is_visible('x',
                             '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/ul/li[5]')  # 选择关闭前台发布主帖
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[3]/button')  # 点保存按钮
        time.sleep(2)
        self.wait_is_visible('x', '/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.scrollbar('400')
        text2 = self.find_element_text("x",'/html/body/div[1]/div/div[3]/div[2]/div[2]')  # 关闭前台发帖无留言按钮，获取页面的提示信息“该留言板已关闭”
        if text2 == u'该留言板已关闭':
            self.deprint(u'留言板关闭前台发布主帖成功')
            result2 = 1
        else:
            self.deprint(u'留言板关闭前台发布主帖失败')
            result2 = 0
        # operlist = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]')
        # divList = operlist.find_elements_by_tag_name("div")
        # # print len(aList)
        # if len(divList) == 2:
        #     self.deprint(u'留言板关闭前台发布主帖成功')
        #     result3 = 1
        # else:
        #     self.deprint(u'留言板关闭前台发布主帖失败')
        #     result3 = 0
        self.close()
        return result2
        # 结束

    def modify_message_adminpost(self):
        # 开始 留言板 13、管理员发帖--14、PC(WAP)端查看,不能编辑和删除
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # time.sleep(2)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[4]/a[1]')  # 点编辑按钮
        self.wait_is_visible('x',
                             '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/button')  # 点主帖限制
        self.wait_is_visible('x',
                             '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/ul/li[1]')  # 选择允许匿名发主帖
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[3]/button')  # 点保存按钮
        time.sleep(1)
        self.scrollbar('200')
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/button[1]')  # 点发帖按钮
        time.sleep(2)
        self.element_value_input('x', '//*[@id="AddPostWindow"]/div/div/div[2]/div[1]/div[1]/div', u'管理员发帖内容')  # 输入发帖内容
        self.wait_is_visible('x',
                             '//*[@id="AddPostWindow"]/div/div/div[3]/div[1]/div[1]/label[1]')  # 选择发帖身份-管理员

        self.wait_is_visible('x', '//*[@id="AddPostWindow"]/div/div/div[3]/div[2]/button')  # 点保存按钮
        # self.driver.refresh()
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div/div[2]/div[4]/a[4]/i')  # 点pc预览
        time.sleep(2)
        # 获取每个帖子的操作按钮数目（管理员 2个，  匿名用户  4个）
        self.driver.switch_to.window(self.driver.window_handles[-1])
        operlist = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div[2]')
        aList = operlist.find_elements_by_tag_name("a")
        # print len(aList)
        if len(aList) == 2:
            self.deprint(u'留言板管理员发帖成功')
            result3 = 1
        else:
            self.deprint(u'留言板管理员发帖失败')
            result3 = 0
        return result3

    def article_relation_reviewarea(self):
        #2、文章管理模块设置关联此评论区，PC（wap)端查看文章时，发表评论
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/span')  # 点评论区设置
        time.sleep(1)
        self.wait_is_visible('x', '//*[@id="boundComment"]/div/div/div[2]/div[2]/div/div/button')  # 点关联评论区下拉框
        self.wait_is_visible('x', '//*[@id="boundComment"]/div/div/div[2]/div[2]/div/div/ul/li[2]')  # 选刚新增的评论区-默认是第一个
        self.wait_is_visible('x', '//*[@id="boundComment"]/div/div/div[3]/button[2]')  # 点确定按钮
        # time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[3]/a')  # 点第一个栏目的标题
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr/td[5]/div/a[2]')  # 点第一个文章的查看
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/section/div[4]/div[1]/span[4]')  # 点发表评论
        title = u'测试发表评论' + self.nowtime()
        self.element_value_input('x', '/html/body/div[1]/section/div[4]/div[2]/textarea', title)  # 输入评论内容
        self.wait_is_visible('x', '/html/body/div[1]/section/div[4]/div[2]/div/div')  # 点提交按钮
        time.sleep(1)
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return title

    def look_reviewarea(self,title):
        # time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.driver.refresh()
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a')  # 点第一个评论区名称
        time.sleep(1)
        self.scrollbar('bottom')
        table1 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody")  #通过xpath获取整个数据行
        trlist = table1.find_elements_by_tag_name("tr")
        print len(trlist)
        if len(trlist) > 0 :
            text2 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[3]/a') #获取第一条数据的主帖内容
            # print str(text2)
            # print title
            if text2 == title :
                self.deprint(u'后台查看评论成功')
                result = 1
            else :
                self.deprint(u'后台查看评论失败')
                result = 0
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return result

    def delete_reviewarea(self):
        # time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[3]/a')  # 点第一个栏目的标题
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr/td[5]/div/a[2]')  # 点第一个文章的查看
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/section/div[5]/div[1]/div[2]/div[2]/span[2]')  # 点第一个评论的删除
        time.sleep(2)
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def modify_review_limitlogin(self):
        #开始 评论区 -9、修改为仅登；录后发帖--10、未登录状态下进入PC(WAP)端发帖，跳转到登录页面-
        # time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a') #点评论区名称链接
        time.sleep(10)
        text4 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div/span')  #获取总贴数

        if text4 == '0' :
            r2 = 1
            self.deprint(u"后台查看删帖成功")
        else :
            r2 = 0
            self.deprint(u"后台查看删帖失败")
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[4]/a[1]')  # 点编辑按钮
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/button')  # 点主帖限制
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/ul/li[4]')  # 选择仅登录可以发主帖
        time.sleep(2)
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[2]/button')  # 点请选择注册表单
        self.wait_is_visible('x','//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[2]/ul/li[2]')  # 选择新建注册表单(9)
        self.wait_is_visible('x','//*[@id="editforum"]/div/div/div[3]/button')  # 点保存按钮
        time.sleep(2)
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        choose = ChoosePage(self.driver)
        choose.click_menu_bt('22')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[3]/a')  # 点第一个栏目的标题
        time.sleep(2)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr/td[5]/div/a[2]')  # 点第一个文章的查看
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/section/div[4]/div[1]/span[4]')  # 点发表评论
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        text1 = self.find_element_text("x", '//*[@id="one1"]') #未登录发帖跳到登陆界面，获取到登陆页面的显示文字“普通登录”
        # print str(text1)
        if text1.replace(' ','') == u'普通登录' :
            self.element_value_input('x', '//*[@id="con_one_1"]/div[1]/input','18732159800')  # 输入用户名
            self.element_value_input('x', '//*[@id="con_one_1"]/div[3]/input', '123123')  # 输入密码
            self.wait_is_visible('x', '//*[@id="con_one_1"]/input')  # 点登陆按钮
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.wait_is_visible('x', '/html/body/div[1]/section/div[4]/div[1]/span[4]')  # 点发表评论
            time.sleep(2)
            title = u'测试发表评论' + self.nowtime()
            self.element_value_input('x', '/html/body/div[1]/section/div[4]/div[2]/textarea', u'测试发表评论')  # 输入评论内容
            self.wait_is_visible('x', '/html/body/div[1]/section/div[4]/div[2]/div/div')  # 点提交按钮
            self.driver.refresh()
            time.sleep(3)
            text4 = self.find_element_text("x", '/html/body/div[1]/section/div[4]/div[1]/span[3]') #获取评论数目
            if text4.replace(' ','') == '1' :
                self.deprint(u'仅登录可以发主帖成功')
                result1 = 1
            else :
                self.deprint(u'仅登录可以发主帖失败')
                result1 = 0
        else :
            self.deprint(u'仅登录可以发主帖失败')
            result1 = 0
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return r2,result1
        # 结束

    def modify_review_adminpost(self):
        # 开始 评论区 13、管理员发帖--14、PC(WAP)端查看,不能编辑和删除
        # time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a')  # 点第一个评论区的名称
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[4]/a[1]')  # 点编辑按钮
        self.wait_is_visible('x',
                             '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/button')  # 点主帖限制
        self.wait_is_visible('x',
                             '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/ul/li[1]')  # 选择允许匿名发主帖
        self.wait_is_visible('x', '//*[@id="editforum"]/div/div/div[3]/button')  # 点保存按钮
        time.sleep(2)
        self.scrollbar('200')
        text1 = self.find_element_text("x", '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[4]/a')  # 获取第一条数据的所属子版
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/button[1]')  # 点发帖按钮
        time.sleep(1)
        self.element_value_input('x', '//*[@id="addModal"]/div/div/div[2]/div[1]/input', text1)  # 输入发帖内容
        self.wait_is_visible('x', '//*[@id="addModal"]/div/div/div[2]/div[1]/ul/li')  # 点模糊查询出的子版
        self.element_value_input('x', '//*[@id="addModal"]/div/div/div[2]/div[2]/div[1]/div', u'自动化测试')  # 输入发帖内容
        self.wait_is_visible('x',
                             '//*[@id="addModal"]/div/div/div[3]/div/div[1]/label[1]')  # 选择发帖身份-管理员

        self.wait_is_visible('x', '//*[@id="addModal"]/div/div/div[3]/button')  # 点保存按钮
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        choose = ChoosePage(self.driver)
        choose.click_menu_bt('22')
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[3]/a')  # 点第一个栏目的标题
        time.sleep(1)
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr/td[5]/div/a[2]')  # 点第一个文章的查看
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        rowdata = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[5]/div[1]/div[2]/div[2]')#获取删除所在行的显示数据
        spanlist = rowdata.find_elements_by_tag_name("span")
        # print len(spanlist)
        if len(spanlist) == 2:
            self.deprint(u'评论区管理员发帖成功')
            result3 = 1
        else:
            self.deprint(u'评论区管理员发帖失败')
            result3 = 0

        return result3

    def nameofform(self, form_name):

        # #点击选择
        # self.element_click('x', '//*[@id="createSeminarScroller"]/form/div[8]/div[2]/div/button/span')

        for num in range(1, 100):  #遍历选项，选中form_name 因为遍历100遍，及100个下表元素。如果没有正确选中，很有可能找不到元素，报错。
            ele = '//*[@id="editforum"]/div/div/div[2]/div/form/div[3]/div[2]/div[2]/ul/li[' + str(num) + ']'
            # print "ele:",ele
            all_form_name = self.find_element_text("x", ele)  # 获各个注册单名称
            # print "all_form_name:",all_form_name
            if all_form_name == form_name:  # 判断对应注册单的名称，点击选择
                self.element_click("x", ele)
                break












if __name__ == '__main__':


    driver = brower()
    login= LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("11")
    form=Create_microdiscussion(driver)
    # form.new_form()
    # form.browse_form()