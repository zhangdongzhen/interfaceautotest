# -*- coding: utf-8 -*-

import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.management_tools.article_pages.section_list_page import SectionListPage


class BrowsePage(BasePage):

    #复制浏览链接地址
    def cope_line(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 移动句柄，对新打开页面进行操作
        o = SectionListPage(self.driver)
        time.sleep(3)
        # current_handle = self.driver.current_window_handle
        # all_handles = self.driver.window_handles
        # url = o.choose_more().encode('unicode-escape').decode('string_escape')
        url = o.choose_more().encode('unicode-escape').decode('string_escape')
        return url

    # 浏览栏目
    def browse_section(self,type):
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 移动句柄，对新打开页面进行操作
        #gm20180820
        newwindow = 'window.open("' + self.cope_line() + '")'
        # newwindow = 'window.open(" + url + ")'
        self.driver.execute_script(newwindow)

        time.sleep(3)
        self.deprint("完成浏览栏目")
        time.sleep(5)
        if type == 0 :
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[-1])
            self.driver.close()
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[-1])



        '''gm20180820
        try:

            # url = wap_url.encode('unicode-escape').decode('string_escape')
                # .encode('unicode-escape').decode("utf-8")
            # url = self.driver.find_element_by_css_selector(
            #     'body > div.g-container-box > div.m-container.ng-scope > div.clearfix.ng-scope > div.vote-link-box > form > div:nth-child(1) > div > input').get_attribute(
            #     "value")

            newwindow = 'window.open("' + self.cope_line() + '")'
            # print newwindow
            # newwindow = 'window.open(" + url + ")'
            self.driver.execute_script(newwindow)
            handles = self.browser.window_handles
            self.browser.switch_to_window(handles[-1])
            time.sleep(3)
            self.deprint("完成浏览栏目")
            time.sleep(3)
            # self.driver.close()
            # # for handle in all_handles:
            # #     if handle == current_handle:
            # #         self.driver.switch_to_window(handle)
            # #         # self.driver.switch_to_window(self.driver.window_handles[1])
            # time.sleep(5)
        except:
            self.deprint("浏览栏目失败")
        '''
        """

        pc_url = self.driver.find_element_by_css_selector(
            'body > div.g-container-box > div.m-container.ng-scope > div.clearfix.ng-scope > div.vote-link-box > form > div:nth-child(1) > div > input').get_attribute(
            "value")
        # print 'pc_url:' + pc_url
        # 新打开一个一个浏览
        # 浏览器 新窗口打开连接
        newwindow = 'window.open("' + pc_url + '")'
        # print newwindow
        driver.execute_script(newwindow)
        # 移动句柄，对新打开页面进行操作
        driver.switch_to.window(driver.window_handles[-1])
         """

    #文章浏览页面的发表评论
    def remark(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转

        self.wait_is_visible('x', '/html/body/div[1]/section/div[4]/div[1]/span[4]')  # 点击评论按钮

        time.sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.element_value_input('x', '/html/body/div[1]/section/div[4]/div[2]/textarea', u'测试')  # 评论框输入内容
        self.wait_is_visible('x', '/html/body/div[1]/section/div[4]/div[2]/div/div')  # 点击提交按钮
        self.deprint(u'发表评论成功')
        self.close()

if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('22')
    # o=SectionListPage(dr)
    # o.choose_firstsection()
    # o.choose_more()
    o = BrowsePage(dr)
    o.cope_line()
    o.browse_section()
    #dr.close()
    time.sleep(3)
    o=SectionListPage(dr)
    o.open_detail_data()

    """
    q=SectionListPage(dr)
    q.choose_firstsection()
    q.create_button_article()
    q.create_article()
    # q.choose_more()
    p = BrowsePage(dr)
    p.cope_line()
    p.browse_section()
    p.remark()
    """
