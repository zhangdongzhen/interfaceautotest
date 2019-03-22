# -*- coding: utf-8 -*-

import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
# from pages.management_tools.article_pages.browse_page import BrowsePage


class SectionListPage(BasePage):

    # 点击新建栏目
    def new_section(self):
        try:
            self.deprint("开始点击新建栏目")
            time.sleep(3)
            # self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/a')  # 点击新建栏目的按钮
            self.deprint("新建栏目按钮成功")
            title = u'automation' + self.nowtime()
            self.find_element_input('x','//*[@id="manageArticleCategoryWindow"]/div[2]/div[1]/div/div/input',title)  #输入栏目名称
            self.wait_is_visible('x', '//*[@class="tags"]/div[2]')
            self.wait_is_visible('x', '//*[@class="tags"]/div[3]/div/span[1]')  # 选择标签
            #self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[11]/div[8]/div/div/div[2]')  #点击“自动化行为标签”
            #self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[11]/div[8]/div/div/div[3]/div[1]/span[1]')  #选择标签
            self.scrollbar("bottom")
            self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div[2]/div[14]/button')  #点击保存按钮
            return title
        except:
            self.deprint("新建栏目失败")

    #删除第一行栏目
    def delete_section(self):
        try:
            self.deprint("开始点击删除栏目")
            time.sleep(3)
            self.find_element_click('x','/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  #点击第一行栏目的更多按钮
            self.find_element_click('x','/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[5]/a')  #点击删除按钮
            time.sleep(1)
            self.find_element_click('x','//*[@id="alertCommon"]/div/div/div[3]/button[2]')  #点击确定按钮
            self.deprint("删除栏目成功")
        except:
            self.deprint("删除栏目失败")

            # 打开数据明细

    #打开详情页面
    def open_detail_data(self):
        try:
            time.sleep(3)
            self.wait_is_visible('x',
                                 '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮
            time.sleep(1)
            self.wait_is_visible('x',
                                 '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[3]/a')  # 点击数据明细按钮
            self.deprint("打开数据明细页面成功")
            time.sleep(5)
            browseNum = self.find_element_text('x',
                                               '/html/body/div[1]/div[1]/div[3]/div/div[3]/div[1]/div/div/span[1]')  # 抓取浏览量
            browseSum = self.find_element_text('x',
                                               '/html/body/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div/span[1]')  # 抓取浏览人数
            self.find_element_click('x', '/html/body/div[1]/div[1]/div[1]/nav/a[2]')  # 返回栏目列表


            # browseNum1 = browseNum.encode("utf-8")
            # browseSum1 = browseSum.encode("utf-8")
            browseNum1 = int(browseNum)
            browseSum1 = int(browseSum)


            #gm20180820
            return browseNum1,browseSum1
        except:
            self.deprint("数据明细页面打开失败")

    # 点击“查看”按钮旁边的更多功能
    def choose_more(self):  # 20180817
        self.deprint("复制浏览链接")
        time.sleep(3)
        self.wait_is_visible('x',
                                '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮
        time.sleep(3)
        self.wait_is_visible('x',
                                '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[2]/a')  # 点击获取链接按钮

        time.sleep(3)
        wap_url = self.find_element_AttributeText('x',
                                                  '//*[@id="copyArticleCategoryLinkWindow"]/div/div/div[2]/div/div/input',
                                                  "value")  # 得到浏览地址

        self.find_element_click('x', '//*[@id="copyArticleCategoryLinkWindow"]/div/div/div[3]/a[2]')  # 点击复制按钮


        self.deprint("复制浏览链接成功")
        return wap_url

    # 点击一个栏目
    def choose_firstsection(self):
        try:
            self.deprint("点击第一个栏目")
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[3]/a')  # 点击第一个栏目按钮
        except:
            self.deprint("点击第一个栏目失败")

    # 点击新建文章按钮
    def create_button_article(self):
        try:
            self.deprint("点击新建文章按钮")
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/a')  # 点击新建文章的按钮
        except:
            self.deprint("点击新建文章按钮失败")

    # 新建文章
    def create_article(self):
        now = int(time.time())
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        title = u'文章' + otherStyleTime
        self.element_value_input('x', '//*[@id="articleTitle"]', u'文章' + otherStyleTime)
        self.element_value_input('x','/html/body',u'测试')#填写正文内容
        self.element_click('x','/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[4]/div/label[1]/span')# 点击“分享设置”的“允许”
        self.scrollbar("100")
        iframe = self.driver.find_element_by_xpath('//*[@id="ueditor_0"]')
        self.driver.switch_to_frame(iframe)
        self.element_value_input('x', '/html/body', u'测试')  # 填写正文内容
        time.sleep(2)
        self.driver.switch_to.default_content()  # 从正文内容输入的iframe窗口切换回主文档
        self.wait_is_visible('x',
                             '/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div[2]')  # 点击便签输入框，进行打标签
        self.wait_is_visible('x',
                             '/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div[3]/div[1]/span[1]')  # 选择“1”的标签
        self.scrollbar("bottom")
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[3]/div')  # 点击保存按钮
        time.sleep(2)
        self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击弹出弹框的“确定”按钮“
        return title

    #查看文章的数据明细
    def look_questionnaire_statistics(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(3)
            self.wait_is_visible('x',
                                 '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮
            time.sleep(1)
            self.wait_is_visible('x',
                                 '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr/td[5]/div/div/ul/li[4]/a')  # 点击数据明细按钮
            self.deprint("打开数据明细页面成功")
            time.sleep(3)
            browseNum = self.find_element_text('x',
                                               '/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/span[1]')  # 抓取浏览量
            browseSum = self.find_element_text('x',
                                               '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/span[1]')  # 抓取浏览人数
            # self.find_element_click('x', '/html/body/div[1]/div[1]/div[1]/nav/a[2]')  # 返回栏目列表


            # browseNum1 = browseNum.encode("utf-8")
            # browseSum1 = browseSum.encode("utf-8")
            browseNum1 = int(browseNum)
            browseSum1 = int(browseSum)


            #gm20180820
            return browseNum1,browseSum1
        except:
            self.deprint("数据明细页面打开失败")


    #查看对应联系人互动及标签触发
    def look_contact_interaction(self,sectionname,actionname):
        self.deprint(u"开始查看对应联系人的互动及标签触发")
        self.deprint(str(sectionname))
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到主界面
        object = ChoosePage(self.driver)
        object.click_menu_bt('17')
        time.sleep(12)
        self.wait_is_visible('x', '/html/body/div[2]/div[2]/div[2]/div[2]/div/button')  # 点查看其它用户
        self.wait_is_visible('x', '//*[@aria-labelledby="dropdownMenu1"]/li/a')  # 点匿名用户
        time.sleep(5)
        self.wait_is_visible('x', '/html/body/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/div[2]/a')  # 点第一个匿名用户的ID
        time.sleep(8)
        iframe = self.driver.find_element_by_xpath("/html/body/div[2]/div[4]/iframe")
        self.driver.switch_to_frame(iframe)
        self.scrollbar("bottom")

        #找到第一个匿名联系人，查看联系人互动记录
        #此页面有时有保存登陆状态，有时没有，造成互动和标签的位置不定
        showtext = self.find_element_text('x',
                                       '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[1]')
        time.sleep(5)
        if showtext == u'触发标签次数排行' :
            # 获取第一行互动记录的互动对象
            text2 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/table/tbody/tr[1]/td[3]')
            time.sleep(1)
            #获取第一行互动记录的互动类型
            text3 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/table/tbody/tr[1]/td[1]')
            time.sleep(1)
            #获取第一行互动记录的互动结果
            text4 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/table/tbody/tr[1]/td[4]/span')
            time.sleep(1)
            if text2 == sectionname and text3 == actionname and text4 == u'成功' :
                self.deprint(u'对应联系人的互动详情成功')
                result1 = 1
            else :
                self.deprint(u'对应联系人的互动详情失败')
                result1 = 0

            #查看联系人标签记录
            #获取第一行互动记录的对象
            text2 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[2]/table/tbody/tr[1]/td[3]')
            #获取第一行互动记录的行为
            text3 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[2]/table/tbody/tr[1]/td[2]')
            #获取第一行互动记录的触发标签
            text4 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[2]/table/tbody/tr[1]/td[4]')
            if text2 == sectionname and text3 == actionname and text4 == '1' :
                self.deprint(u'对应联系人的标签触发成功')
                result2 = 1
            else :
                self.deprint(u'对应联系人的标签触发失败')
                result2 = 0
        else :
            # 获取第一行互动记录的互动对象
            text2 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[1]/div[2]/table/tbody/tr[1]/td[3]')
            time.sleep(1)
            #获取第一行互动记录的互动类型
            text3 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[1]/div[2]/table/tbody/tr[1]/td[1]')
            time.sleep(1)
            #获取第一行互动记录的互动结果
            text4 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[6]/div[1]/div[2]/table/tbody/tr[1]/td[4]/span')
            time.sleep(1)
            if text2 == sectionname and text3 == actionname and text4 == u'成功' :
                self.deprint(u'对应联系人的互动详情成功')
                result1 = 1
            else :
                self.deprint(u'对应联系人的互动详情失败')
                result1 = 0

            #查看联系人标签记录
            #获取第一行互动记录的对象
            text2 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[7]/div[2]/table/tbody/tr[1]/td[3]')
            time.sleep(1)
            #获取第一行互动记录的行为
            text3 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[7]/div[2]/table/tbody/tr[1]/td[2]')
            time.sleep(1)
            #获取第一行互动记录的触发标签
            text4 = self.find_element_text('x', '/html/body/div[1]/div/div[1]/div/div[2]/div[7]/div[2]/table/tbody/tr[1]/td[4]')
            time.sleep(1)
            if text2 == sectionname and text3 == actionname and text4 == '1' :
                self.deprint(u'对应联系人的标签触发成功')
                result2 = 1
            else :
                self.deprint(u'对应联系人的标签触发失败')
                result2 = 0

        if result1 == 1 and result2 == 1:
            return u"查看对应联系人的互动和标签触发成功"
        else:
            return u"查看对应联系人的互动和标签触发失败"


if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('22')
    q=SectionListPage(dr)
    q.choose_firstsection()
    q.create_button_article()
    q.create_article()
    q.choose_more()




    # q.new_section()
    # q.choose_more()
    # object.browse_section()
    # object.open_detail_data()
    # object.delete_section()