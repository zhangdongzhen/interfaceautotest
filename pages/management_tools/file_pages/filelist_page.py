# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
import time

class Filelist_Page(BasePage):

    #共享文件
    def share_file(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        filename = self.find_element_text('x','/html/body/div/div[1]/div[2]/div[6]/table/tbody[2]/tr[1]/td[5]/div/div[1]')#获取第一个新建的文件名字
        self.wait_is_visible('x','/html/body/div/div[1]/div[1]/div/div/a')#新建文件夹后，返回到文件列表页，点击右上方共享文件按钮
        filename1 = self.find_element_text('x','/html/body/div/div[1]/div[2]/div[6]/table/tbody[1]/tr/td[4]/div')#  获取共享文件页面的第一个下载文件的名字
        if filename ==filename1:
            return u'共享文件成功'
        else:
            return u'共享文件失败'

    #下载
    def downlo_file(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        self.wait_is_visible('x','/html/body/div/div[1]/div[2]/div[6]/table/tbody[1]/tr/td[7]/a[1]')#点击第一个文件的下载按钮

    #点击第一个文件名字进入文件详情页
    def click_filename_button(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        filename = self.find_element_text('x','/html/body/div/div[1]/div[2]/div[6]/table/tbody[2]/tr[1]/td[5]/div/div[1]')#获取第一个新建的文件名字
        self.wait_is_visible('x','/html/body/div/div[1]/div[2]/div[6]/table/tbody[2]/tr[1]/td[5]/div/div[1]')
        time.sleep(2)




