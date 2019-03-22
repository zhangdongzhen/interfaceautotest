# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.common_pages.base import BasePage

class Scrollbar_Move():

    def scrollbarmovedown(self):
        # driver = webdriver.Chrome()
        #通过按向下键将页面滚动条拖到底部
        # self.f.find_element_by_xpath("//*[@id='page']/a[10]").send_keys(Keys.DOWN)
        self.element_value_input('x',"//*[@id='page']/a[10]",Keys.DOWN)
        print '将滚动条拉到底端'

    def scrollbarmoveup(self):
        driver = webdriver.Chrome()
        driver.find_element_by_xpath("//*[@id='s_tab']/a[9]").send_keys(Keys.UP)
        print '将滚动条拉到上端'


    def scrollbarmoveup(self):
        driver = webdriver.Chrome()
        driver.find_element_by_xpath("//*[@id='con-ar']/div[3]/a").send_keys(Keys.DOWN)
        print '将滚动条拉到中间'